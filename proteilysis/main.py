from PDBParser import PDBParser, fetch_pdb_file
import json

content = fetch_pdb_file('3GFT')
pdb = PDBParser(content=content)

with open('results.json', 'w') as fout:
        fout.write(json.dumps(pdb.sequence, indent=1))