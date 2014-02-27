#!/usr/bin/env python

from subprocess import call
from sys import argv

def main():

    if len(argv) != 2:
        print "USAGE: install.py [pisces_filename]"
        return

    # remove any previous database
    call('python uninstall.py', shell=True)

    # create a new database
    call('python create_db.py', shell=True)

    # create db tables
    call('python create_db_tables.py', shell=True)

    # fetch pdb files contained in pisces list
    # call('python fetch_pdb_files.py {}'.format(argv[1]), shell=True)

    # parse the previous files for info
    call('python parse_pdb_files.py', shell=True)

    # create all the sql files for data insertion
    call('python mk_sql.py', shell=True)

    # fill in the db
    for sql in ['proteins', 'sequences', 'sheets', 'helices']:
        call('python fill_db.py db_{}.sql'.format(sql), shell=True)



if __name__ == "__main__":
    main()