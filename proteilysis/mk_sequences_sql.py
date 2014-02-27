#!/usr/bin/env python

import os
import config
import json


def main():
    with open(config.FILENAMES['SEQ_SQL'], 'w') as sql_file:

        for root, dirs, files in os.walk(config.PATHS['SEQUENCE_DIR']):
            for filename in files:
                with open(os.path.join(config.PATHS['SEQUENCE_DIR'], 
                            filename)) as fin:

                    try:
                        sequences = json.loads(fin.read())
                    except ValueError:  # ignore not json files
                        continue

                    for seq in sequences:
                        sql_file.write(config.SQL_TEMPLATES['INSERT_SEQ'].format(
                            proteinID=1,  # TODO temporary
                            serNum=seq['serNum'],
                            chainID=seq['chainID'],
                            numRes=seq['numRes'],
                            residues="-".join(seq['residues'])
                        ))


if __name__ == "__main__":
    main()