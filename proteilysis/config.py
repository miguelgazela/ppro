#!/usr/bin/env python

DEBUG = True


PATHS = {
    'PDB_FILE_DIR': 'pdb_files',
    'PARSED_INFO_DIRS': [
        'pdb_helices',
        'pdb_sheets',
        'pdb_sequences'
    ],
    'HELICES_DIR': 'pdb_helices',
    'SHEETS_DIR': 'pdb_sheets',
    'SEQUENCE_DIR': 'pdb_sequences',
    'SQL_DIR': 'sql_files',
}


FILENAMES = {
    'PROTEINS_SQL': 'db_proteins.sql',
    'HELICES_SQL': 'db_helices.sql',
    'SHEETS_SQL': 'db_sheets.sql',
    'SEQ_SQL': 'db_sequences.sql',
}


SQL_TEMPLATES = {
    'INSERT_PROTEIN': "INSERT INTO Protein (structureID, accID) VALUES ('{structureID}', '{accID}');\n",

    'INSERT_HELIX': "INSERT INTO Helix (structureID, helixClass, endICode, helixID, endSeqNum, initSeqNum, initResName, serNum, initChainID, initICode, length, endChainID, endResName, type) VALUES ('{structureID}', {helixClass}, '{endICode}', '{helixID}', {endSeqNum}, {initSeqNum}, '{initResName}', {serNum}, '{initChainID}', '{initICode}', {length}, '{endChainID}', '{endResName}', '{type}');\n",

    'INSERT_COMPLETE_SHEET': "INSERT INTO Sheet (structureID, strand, sheetID, numStrands, initResName, initChainID, initSeqNum, initICode, endResName, endChainID, endSeqNum, endICode, sense, curAtom, curResName, curChainID, curResSeq, curICode, prevAtom, prevResName, prevChainID, prevResSeq, prevICode) VALUES ('{structureID}', {strand}, '{sheetID}', {numStrands}, '{initResName}', '{initChainID}', {initSeqNum}, '{initICode}', '{endResName}', '{endChainID}', {endSeqNum}, '{endICode}', {sense}, '{curAtom}', '{curResName}', '{curChainID}', {curResSeq}, '{curICode}', '{prevAtom}', '{prevResName}', '{prevChainID}', {prevResSeq}, '{prevICode}');\n",
    'INSERT_INCOMPLETE_SHEET': "INSERT INTO Sheet (structureID, strand, sheetID, numStrands, initResName, initChainID, initSeqNum, initICode, endResName, endChainID, endSeqNum, endICode, sense) VALUES ('{structureID}', {strand}, '{sheetID}', {numStrands}, '{initResName}', '{initChainID}', {initSeqNum}, '{initICode}', '{endResName}', '{endChainID}', {endSeqNum}, '{endICode}', {sense});\n",

    'INSERT_SEQ': "INSERT INTO Sequence (structureID, serNum, chainID, numRes, residues) VALUES ('{structureID}', {serNum}, '{chainID}', {numRes}, '{residues}');\n"
}


# Database settings

DATABASE = {
    'name': 'proteilysis',
    'username': 'root',
    'root_pass': 'BKsrUgn6',
    'db_user': 'user1',
    'db_user_pass': 'password',
}