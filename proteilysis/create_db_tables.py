#!/usr/bin/env python

from subprocess import call
import config

def main():
    call('cat sql_files/db_def.sql | mysql --user={user} \
        --password={user_pass} {db}'.format(
            user=config.DATABASE['db_user'],
            user_pass=config.DATABASE['db_user_pass'],
            db=config.DATABASE['name']),
        shell=True)


if __name__ == "__main__":
    main()