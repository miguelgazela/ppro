from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.crypto import get_random_string
from django.core.serializers.json import DjangoJSONEncoder

from proteil.models import Protein, Structure, Helix, Sequence, Sheet
from proteil.forms import UploadFile, UploadListIds
from Parsers import utils, PdbParser, UnitprotParser
from proteil import settings

import os
from datetime import datetime
import json
import re

# Create your views here.

def index(request):
	return render(request, 'proteil/index.html')


def protein_add(request):
	uploadPiscesForm = UploadFile()
	uploadListIds = UploadListIds()
	return render(request, 'proteil/proteins/new.html', 
		{'pisces_form': uploadPiscesForm, 'list_form': uploadListIds})


def upload_pisces_file(request):
	if request.method == 'POST':
		form = UploadFile(request.POST, request.FILES)
		if form.is_valid():
			result = handle_uploaded_file(request.FILES['file'])

			if result['status'] == "success":
				con = {}
				con['existing_ids'] = []
				con['non_existing_ids'] = []
				con['total'] = len(result['payload'])

				for id in result['payload']:
					try:
						structure = Structure.objects.get(pdb_id=id)
						con['existing_ids'].append(id)
					except Structure.DoesNotExist:
						con['non_existing_ids'].append(id)

				return render(request, 'proteil/proteins/ids_list.html', con)
			return HttpResponse(result['error_msg'])
	else:
		return redirect('protein_add')

	return render(request, 'proteil/proteins/new.html', {'pisces_form': form})
      

def upload_ids_list(request):
	if request.method == 'POST':
		form = UploadListIds(request.POST)
		if form.is_valid():
			result = handle_uploaded_list_ids(form.cleaned_data)

			if result['status'] == "success":
				con = {}
				con['existing_ids'] = []
				con['non_existing_ids'] = []
				con['total'] = len(result['payload'])

				for id in result['payload']:
					try:
						if form.cleaned_data['ids_type'] == "pdb":
							Structure = Structure.objects.get(pdb_id=id)
						else:
							pass
						con['existing_ids'].append(id)
					except Structure.DoesNotExist:
						con['non_existing_ids'].append(id)

				return render(request, 'proteil/proteins/ids_list.html', con)
			return HttpResponse(result['error_msg'])
	else:
		return redirect('protein_add')

	return render(request, 'proteil/proteins/new.html', {'ids_list_form': form})


def add_protein(request, id):
	response = {
		"status": "error",
		"error_msg": "",
	}

	if request.is_ajax():
		if re.search(r'^[A-Za-z0-9]{4}$', id):
			add_by_pdb(response, id)
		elif re.search(r'^[A-Za-z0-9]{6}$', id):
			add_by_uniprotkb(response, id)
	else:
		response["error_msg"] = "API can only be used with AJAX requests";

	return HttpResponse(json.dumps(response), content_type="application/json")

class ProteinList(ListView):
	model = Protein
	template_name = "proteil/proteins/protein_list.html"
	context_object_name = "proteins"
	queryset = Protein.objects.order_by('uniprotkb_id')


def add_by_pdb(response, pdb_id):
	content = utils.fetch_pdb_file(pdb_id)

	if content:
		try:
			parser = PdbParser(pdb_id, content)
			uniprotkbIds = utils.idmapping(pdb_id, True)

			structure = Structure(
				pdb_id=pdb_id,
				classification=parser.classification,
				title=parser.title
			)
			
			structure.save()

			if uniprotkbIds:
				protein = Protein(uniprotkb_id=uniprotkbIds[0])
				protein.save()
				structure.protein = protein

			for h in parser.helices:
				helix = Helix(
					comment=h['comment'],
					helix_class=h['helixClass'],
					end_i_code=h['endICode'],
					helix_id=h['helixID'],
					end_seq_num=h['endSeqNum'],
					init_seq_num=h['initSeqNum'],
					init_res_name=h['initResName'],
					ser_num=h['serNum'],
					init_chain_id=h['initChainID'],
					init_i_code=h['initICode'],
					length=h['length'],
					end_chain_id=h['endChainID'],
					end_res_name=h['endResName'],
					classification=h['helixClass']
				)
				helix.structure = structure
				helix.save()

			for s in parser.sequence:
				sequence = Sequence(
					chain_id=s['chainID'],
					num_res=s['numRes'],
					residues=s['residues']
				)
				sequence.structure = structure
				sequence.save()

			for s in parser.sheets:
				sheet = Sheet(
					strand=s['strand'],
					sheet_id=s['sheetID'],
					numStrands=s['numStrands'],
					init_res_name=s['initResName'],
					init_chain_id=s['initChainID'],
					init_seq_num=s['initSeqNum'],
					init_i_code=s['initICode'],
					end_res_name=s['endResName'],
					end_chain_id=s['endChainID'],
					end_seq_num=s['endSeqNum'],
					end_i_code=s['endICode'],
					sense=s['sense']
				)
				sheet.structure = structure

				if sheet.sense != 0:
					sheet.cur_atom = s['curAtom']
					sheet.cur_res_name = s['curResName']
					sheet.cur_chain_id = s['curChainID']
					sheet.cur_res_seq = s['curResSeq']
					sheet.cur_i_code = s['curICode']
					sheet.prev_atom = s['prevAtom']
					sheet.prev_res_name = s['prevResName']
					sheet.prev_chain_id = s['prevChainID']
					sheet.prev_res_seq = s['prevResSeq']
					sheet.prev_i_code = s['prevICode']

				sheet.save()

			response['status'] = "success"
			response['uniprotkbId'] = uniprotkbIds[0];

		except Exception, e:
			response['status'] = "error"
			response['error_msg'] = str(e) # debug mode only
	else:
		response['error_msg'] = "PDB file not found"


def add_by_uniprotkb(response, uniprotkb_id):
	pass


def handle_uploaded_file(f):
	result = {}

	# get possible list of protein structures
	ids = utils.parse_pisces_file(f)
	if not ids:
		result['status'] = "error"
		result['error_msg'] = "Not a valid file. No ids recognized."
		return result

	f.seek(0)
	
	# create dir for pdb files
	if not os.path.isdir(settings.PATHS['UPLOADS']):
		os.mkdir(settings.PATHS['UPLOADS'])

	filename = get_random_string(16, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") 
	with open(os.path.join(settings.PATHS['UPLOADS'], filename), "w") as fout:
		fout.write(f.read())

	result['status'] = "success"
	result['payload'] = ids
	return result


def handle_uploaded_list_ids(data):
	result = {}

	ids = utils.parse_list_ids(data['ids'], data['ids_type'])
	
	if not ids:
		result['status'] = "error"
		result['error_msg'] = "Invalid input. No ids recognized."
	else:
		result['status'] = "success"
		result['payload'] = ids

	return result


