#!/usr/bin/env python

import os
import config
from PDBParser import utils
from os.path import join as pjoin

def main():
	if not os.path.isdir(config.PATHS['SQL_DIR']):
		os.mkdir(config.PATHS['SQL_DIR'])

	with open(pjoin(config.PATHS['SQL_DIR'], config.FILENAMES['PROTEINS_SQL']), 'w') as sql_file:

		for root, dirs, files in os.walk(config.PATHS['PDB_FILE_DIR']):
			for filename in files:
				sql_file.write(config.SQL_TEMPLATES['INSERT_PROTEIN'].format(
					pdbId=filename,
					uniprotkbId=utils.idmapping(filename)
				))

if __name__ == "__main__":
	main()