#!/usr/bin/env python

import os
from os.path import join as pjoin
import json
from PDBParser import PDBParser
import config


def create_dirs():
    """
    Creates directories for the parsed information of the
    protein structures.
    """

    for f_dir in config.PATHS['PARSED_INFO_DIRS']:
        if not os.path.isdir(f_dir):
            os.mkdir(f_dir)


def save_json(path, data):
    with open(path, 'w') as fout:
        fout.write(json.dumps(data, indent=1))


def main():
    
    # check if directory with pdb files exists
    if not os.path.isdir(config.PATHS['PDB_FILE_DIR']):
        print "Directory with PDB files was not found. \
            Run the script 'fetchListPDBFiles.py' first."
        return -1

    create_dirs()

    # loop over each file and parse it
    for root, dirs, files in os.walk(config.PATHS['PDB_FILE_DIR']):
        for filename in files:
            with open(pjoin(config.PATHS['PDB_FILE_DIR'], filename)) as fin:
                content = fin.read()
            
            parser = PDBParser(content)
            save_json(pjoin(config.PATHS['HELICES_DIR'], filename), parser.helices)
            save_json(pjoin(config.PATHS['SHEETS_DIR'], filename), parser.sheets)
            save_json(pjoin(config.PATHS['SEQUENCE_DIR'], filename), parser.sequence)
            


if __name__ == "__main__":
    main()