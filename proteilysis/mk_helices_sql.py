#!/usr/bin/env python

import os
import config
import json


HELIX_TYPES = {
    '0': 'Right-handed alpha (default)',
    '1': 'Right-handed alpha (default)',
    '2': 'Right-handed omega',
    '3': 'Right-handed pi',
    '4': 'Right-handed gamma',
    '5': 'Right-handed 3 - 10',
    '6': 'Left-handed alpha',
    '7': 'Left-handed omega',
    '8': 'Left-handed gamma',
    '9': '2 - 7 ribbon/helix',
    '10': 'Polyproline' 
}


def main():
    with open(config.FILENAMES['HELICES_SQL'], 'w') as sql_file:
        for root, dirs, files in os.walk(config.PATHS['HELICES_DIR']):
            for filename in files:
                with open(os.path.join(config.PATHS['HELICES_DIR'], 
                            filename)) as fin:

                    try:
                        protein_helices = json.loads(fin.read())
                    except ValueError:  # ignore not json files
                        continue

                    for helix in protein_helices:

                        helix_type = HELIX_TYPES[str(helix['helixClass'])]
                        sql_file.write(config.SQL_TEMPLATES['INSERT_HELIX'].format(
                            structureID=helix['structureID'],
                            comment=helix['comment'],
                            helixClass=helix['helixClass'],
                            endICode=helix['endICode'],
                            helixID=helix['helixID'],
                            endSeqNum=helix['endSeqNum'],
                            initSeqNum=helix['initSeqNum'],
                            initResName=helix['initResName'],
                            serNum=helix['serNum'],
                            initChainID=helix['initChainID'],
                            initICode=helix['initICode'],
                            length=helix['length'],
                            endChainID=helix['endChainID'],
                            endResName=helix['endResName'],
                            type=helix_type
                        ))


if __name__ == "__main__":
    main()