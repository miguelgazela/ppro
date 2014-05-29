from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.crypto import get_random_string

from proteil.models import Protein
from proteil.forms import UploadFile
from PdbParser import utils
from proteil import settings

import os
from datetime import datetime

# Create your views here.

def index(request):
	return render(request, 'proteil/index.html')


def protein_add(request):
	uploadPiscesForm = UploadFile()
	return render(request, 'proteil/proteins/new.html', {'pisces_form': uploadPiscesForm})


def upload_pisces_file(request):
	if request.method == 'POST':
		form = UploadFile(request.POST, request.FILES)
		if form.is_valid():
			result = handle_uploaded_file(request.FILES['file'])

			if result['status'] == "success":
				ids = []
				existing = 0

				for id in result['payload']:
					try:
						protein = Protein.objects.get(pdbId=id)
						ids.append({'id': id, 'exists': True})
						existing += 1
					except Protein.DoesNotExist:
						ids.append({'id': id, 'exists': False})

				return render(request, 'proteil/pisces/ids_list.html', {'ids': ids, 'existing': existing})
			return HttpResponse(result['error_msg'])

	return render(request, 'proteil/proteins/new.html', {'pisces_form': form})
        	


class ProteinList(ListView):
	model = Protein
	template_name = "proteil/proteins/protein_list.html"
	context_object_name = "proteins"


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
