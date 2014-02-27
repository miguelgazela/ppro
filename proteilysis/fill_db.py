#!/usr/bin/env python

from subprocess import call
from sys import argv
from config import DATABASE as DB

def main():
    if len(argv) != 2:
        print "USAGE: fill_db.py [sql_filename]"
        return

    call('mysql --user={user} --password={user_pass} {db} < {sql}'.format(
            user=DB['db_user'],
            user_pass=DB['db_user_pass'],
            db=DB['name'],
            sql=argv[1]
        ), shell=True)


if __name__ == "__main__":
    main()