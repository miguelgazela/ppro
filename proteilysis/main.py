from PDBParser import PDBParser, fetch_pdb_file

content = fetch_pdb_file('3GFT')
pdb = PDBParser(content=content)

print pdb.sequence