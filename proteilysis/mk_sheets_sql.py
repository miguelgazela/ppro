#!/usr/bin/env python

import os
import config
import json


def main():
    with open(config.FILENAMES['SHEETS_SQL'], 'w') as sql_file:
        for root, dirs, files in os.walk(config.PATHS['SHEETS_DIR']):
            for filename in files:
                with open(os.path.join(config.PATHS['SHEETS_DIR'], 
                            filename)) as fin:

                    try:
                        sheets = json.loads(fin.read())
                    except ValueError:
                        continue

                    for sheet in sheets:
                        if sheet['sense'] == 0:
                            sql_file.write(
                                config.SQL_TEMPLATES['INSERT_INCOMPLETE_SHEET'].format(
                                    proteinID=1, # TODO temporary fix
                                    numStrands=sheet['numStrands'],
                                    endICode=sheet['endICode'],
                                    sense=sheet['sense'],
                                    initChainID=sheet['initChainID'],
                                    initSeqNum=sheet['initSeqNum'],
                                    initResName=sheet['initResName'],
                                    endSeqNum=sheet['endSeqNum'],
                                    initICode=sheet['initICode'],
                                    endChainID=sheet['endChainID'],
                                    strand=sheet['strand'],
                                    endResName=sheet['endResName'],
                                    sheetID=sheet['sheetID']
                            ))
                        else:
                            sql_file.write(
                                config.SQL_TEMPLATES['INSERT_COMPLETE_SHEET'].format(
                                    proteinID=1, # TODO temporary fix
                                    numStrands=sheet['numStrands'],
                                    endICode=sheet['endICode'],
                                    sense=sheet['sense'],
                                    initChainID=sheet['initChainID'],
                                    initSeqNum=sheet['initSeqNum'],
                                    initResName=sheet['initResName'],
                                    endSeqNum=sheet['endSeqNum'],
                                    initICode=sheet['initICode'],
                                    endChainID=sheet['endChainID'],
                                    strand=sheet['strand'],
                                    endResName=sheet['endResName'],
                                    sheetID=sheet['sheetID'],
                                    curAtom=sheet['curAtom'],
                                    curResName=sheet['curResName'],
                                    curChainID=sheet['curChainID'],
                                    curResSeq=sheet['curResSeq'],
                                    curICode=sheet['curICode'],
                                    prevAtom=sheet['prevAtom'],
                                    prevResName=sheet['prevResName'],
                                    prevChainID=sheet['prevChainID'],
                                    prevResSeq=sheet['prevResSeq'],
                                    prevICode=sheet['prevICode']
                            ))


if __name__ == "__main__":
    main()