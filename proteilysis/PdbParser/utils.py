#!/usr/bin/env python

import requests
import re
import constants as const

def fetch_pdb_file(id):
    """
    Returns the content of a pdb file if it exists or None if it doesn't
    """
    content = requests.get("%s/%s.pdb" % (const.BASE_URL, id))
    
    if not content.url == const.NO_SUCH_FILE_URL:
        return content.text
    return None


def parse_pisces_file(f):
    """
    
    """
    
    try:
        lines = f.read().splitlines()
        return [line.strip()[:4]
                for line in lines if re.search('^[A-Z0-9]{5}', line)]
    except IOError:
        return None


def idmapping(id):
    """
    Does the mapping of a pdb id to a UniProtKB id and returns it
    """
    content = requests.get(const.ID_MAPPING_URL,
        params={'from': 'PDB_ID', 'to': 'ACC', 'format': 'tab', 'query': id})
    
    content = content.text.split()

    if content[-1] != 'To':
        return content[-1]
    else:
        return ""


    