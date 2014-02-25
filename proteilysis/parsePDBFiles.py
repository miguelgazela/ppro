#!/usr/bin/env python

import os
from os.path import join as pjoin
import json
from libs.PDBParser import PDBParser
from config import config


def create_dirs():
    """
    Creates directories for the parsed information of the
    protein structures.
    """

    for f_dir in config['PARSED_INFO_DIRS']:
        if not os.path.isdir(f_dir):
            os.mkdir(f_dir)


def save_json(path, data):
    with open(path, 'w') as fout:
        fout.write(json.dumps(data, indent=1))


def main():
    
    # check if directory with pdb files exists
    if not os.path.isdir(config['PDB_FILE_DIR']):
        print "Directory with PDB files was not found. \
            Run the script 'fetchListPDBFiles.py' first."
        return -1

    create_dirs()

    # loop over each file and parse it
    for root, dirs, files in os.walk(config['PDB_FILE_DIR']):
        for filename in files:
            with open(pjoin(config['PDB_FILE_DIR'], filename)) as fin:
                content = fin.read()
            
            parser = PDBParser(content)
            save_json(pjoin(config['HELICES_DIR'], filename), parser.helices)
            save_json(pjoin(config['SHEETS_DIR'], filename), parser.sheets)
            save_json(pjoin(config['SEQUENCE_DIR'], filename), parser.sequence)
            


if __name__ == "__main__":
    main()