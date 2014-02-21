from django.shortcuts import render
from libs.PDBParser import PDBParser, fetch_pdb_file
import json
import requests
from lxml import etree

def index(request):
    if request.method == "GET":
        return render(request, 'protein_folding_analysis/index.html')
    elif request.method == "POST":

        protein_id = request.POST.get('protein_id')
        pdb = fetch_pdb_file(protein_id)
        data = None

        if not pdb is None:
            parser = PDBParser(pdb)
            description_xml = requests.get(
                'http://www.rcsb.org/pdb/rest/describePDB?structureId=%s' 
                % protein_id
            ).text
            root = etree.fromstring(description_xml)

            pdb_xml = root[0]
            pdb = {
                'title': pdb_xml.get('title'),
                'id': pdb_xml.get('structureId'),
                'keywords': pdb_xml.get('keywords'),
                'nr_residues': pdb_xml.get('nr_residues'),
                'nr_atoms': pdb_xml.get('nr_atoms'),
                'structure_authors': pdb_xml.get('structure_authors'), 
            }

            data = json.dumps(parser.sequence, indent=1)

        return render(request, 'protein_folding_analysis/index.html',
            {'data': data, 'pdb': pdb}
        )
