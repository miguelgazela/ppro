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
}


FILENAMES = {
    'PROTEINS_SQL': 'db_proteins.sql',
    'HELICES_SQL': 'db_helices.sql',
}


SQL_TEMPLATES = {
    'INSERT_PROTEIN': "INSERT INTO Protein (structureID, pdbPath) VALUES ('{0}', '{1}');\n",
    'INSERT_HELIX': "INSERT INTO Helix (proteinID, helixClass, endICode, helixID, endSeqNum, initSeqNum, initResName, serNum, initChainID, initICode, length, endChainID, endResName, type) VALUES ({proteinID}, {helixClass}, '{endICode}', '{helixID}', {endSeqNum}, {initSeqNum}, '{initResName}', {serNum}, '{initChainID}', '{initICode}', {length}, '{endChainID}', '{endResName}', '{type}');\n"
}


# Database settings

DATABASE = {
    'name': 'proteilysis',
    'username': 'root',
    'root_pass': 'BKsrUgn6',
    'db_user': 'user1',
    'db_user_pass': 'password',
}