#!/usr/bin/env python

import os
from sys import argv
from libs.PDBParser import utils
from config import config

PDB_FILES_DIR = "pdb_files"


def usage():
    print "USAGE: script1.py [filename]"


def main():
    if len(argv) != 2:
        return usage()

    # get the list of protein structures id's
    ids = utils.parse_pisces_file(argv[1])
    if ids:
        print "The file '{0}' was not found.".format(argv[1])
        return -1

    # if not exists create dir for pdb_files
    if not os.path.isdir(PDB_FILES_DIR):
        os.mkdir(PDB_FILES_DIR)

    # get each pdb file from rcsb.org
    counter = 1
    for struct_id in ids:
        content = utils.fetch_pdb_file(struct_id)

        # check if file existed
        if content:
            with open(os.path.join(PDB_FILES_DIR, struct_id), 'w') as fout:
                fout.write(content)

            if config['debug_mode']:
                print "Fetched {0} - {1}/{2}".format(struct_id, counter, len(ids))
                counter += 1


if __name__ == "__main__":
    main()