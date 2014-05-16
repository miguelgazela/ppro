#!/usr/bin/env python

from subprocess import call
from sys import argv
import config

def main():

    if len(argv) != 2:
        print "USAGE: install.py [pisces_filename]"
        return

    # remove any previous database
    if config.DEBUG:
        print '> 1. Removing any previous DB'
    call('python uninstall.py', shell=True)

    # create a new database
    if config.DEBUG:
        print '> 2. Creating new DB'
    call('python create_db.py', shell=True)

    # create db tables
    if config.DEBUG:
        print '> 3. Creating DB tables'
    call('python create_db_tables.py', shell=True)

    # fetch pdb files contained in pisces list
    if config.DEBUG:
        print '> 4. Fetching pdb files from rcsb.org'
    # call('python fetch_pdb_files.py {}'.format(argv[1]), shell=True)

    # parse the previous files for info
    if config.DEBUG:
        print '> 5. Parsing pdb files'
    call('python parse_pdb_files.py', shell=True)

    # create all the sql files for data insertion
    if config.DEBUG:
        print '> 6. Creating sql files for the parsed data'
    call('python mk_sql.py', shell=True)

    # fill in the db
    if config.DEBUG:
        print '> 7. Filling the DB with the sql'
    for sql in ['proteins', 'sequences', 'sheets', 'helices']:
        call('python fill_db.py sql_files/db_{}.sql'.format(sql), shell=True)


if __name__ == "__main__":
    main()