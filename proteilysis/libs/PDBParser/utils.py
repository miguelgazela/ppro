#!/usr/bin/env python

import requests
import re
from constants import BASE_URL, NO_SUCH_FILE_URL

def fetch_pdb_file(id):
    """
    Returns the content of a pdb file if it exists or None if it doesn't
    """
    content = requests.get("%s/%s.pdb" % (BASE_URL, id))
    
    if not content.url == NO_SUCH_FILE_URL:
        return content.text
    return None


def parse_pisces_file(filename):
    """
    Parses the given filename and returns the list of protein
    structures ids contained in it, or None if the file doesn't
    exist.
    """
    
    try:
        with open(filename) as fin:
            lines = fin.read().splitlines()
            return [line.strip()[:4]
                        for line in lines if re.search('^[A-Z0-9]{5}', line)]
    except IOError:
        return None


    
