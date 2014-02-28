#!/usr/bin/env python

from subprocess import call
import config

def main():

    # create the database
    if config.DEBUG:
        print 'STEP 1. Creating new DB'

    call('mysqladmin -u root --password={root_pass} create {db}'.format(
            root_pass=config.DATABASE['root_pass'], db=config.DATABASE['name']
        ), shell=True)

    # creating user responsible for managing the database
    if config.DEBUG:
        print 'STEP 2. Creating user %s, manager of the DB' \
            % (config.DATABASE['db_user'])

    call('echo "GRANT ALL PRIVILEGES ON {db}.* TO {user}@localhost IDENTIFIED BY \'{user_pass}\';" | mysql -u root --password={root_pass} mysql'.format(
            db=config.DATABASE['name'],
            user=config.DATABASE['db_user'],
            user_pass=config.DATABASE['db_user_pass'],
            root_pass=config.DATABASE['root_pass']), shell=True)

if __name__ == "__main__":
    main()