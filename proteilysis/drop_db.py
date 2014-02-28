#!/usr/bin/env python

from subprocess import call
from config import DATABASE as DB


def main():
    # drop database
    call('mysqladmin -u root --password={root_pass} drop {db}'.format(
        root_pass=DB['root_pass'], db=DB['name']), shell=True)


if __name__ == "__main__":
    main()