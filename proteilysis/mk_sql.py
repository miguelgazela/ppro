#!/usr/bin/env python

from subprocess import call
import os
import re

def main():

    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            if re.search('^mk_[a-z]+_sql.py$', filename):
                call('python {}'.format(filename), shell=True)

if __name__ == "__main__":
    main()