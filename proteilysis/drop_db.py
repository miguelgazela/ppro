#!/usr/bin/env python

from subprocess import call
import config

def main():
    # drop database
    call([
        'mysqladmin',
        '-u',
        'root',
        '--password={}'.format(config.DATABASE['root_pass']),
        'drop',
        config.DATABASE['name']
    ])


if __name__ == "__main__":
    main()