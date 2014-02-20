from django.shortcuts import render
from libs.PDBParser import PDBParser, fetch_pdb_file
import json

def index(request):
    if request.method == "GET":
        return render(request, 'protein_folding_analysis/index.html')
    elif request.method == "POST":

        protein_id = request.POST.get('protein_id')
        pdb = fetch_pdb_file(protein_id)
        data = None

        if not pdb is None:
            parser = PDBParser(pdb)
            data = json.dumps(parser.sequence, indent=1)

        return render(request, 'protein_folding_analysis/index.html',
            {'data': data, 'id': protein_id }
        )
