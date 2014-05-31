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


def idmapping(id, is_pdb):
    """
    Does the mapping of a id to another type of id and returns it
    """
    if is_pdb:
        content = requests.get(const.ID_MAPPING_URL,
            params={'from': 'PDB_ID', 'to': 'ACC', 'format': 'tab', 'query': id})
    else:
        content = requests.get(const.ID_MAPPING_URL,
            params={'from': 'ACC', 'to': 'PDB_ID', 'format': 'tab', 'query': id})
    
    content = content.text.split()

    if content[-1] != 'To':
        return content[3::2]
    else:
        return [""]


def parse_list_ids(list, type):
    try:
        regex = type == "pdb" and r"^([A-Za-z0-9]{4})" or r"^([A-Za-z0-9]{6})"
        lines = list.splitlines()
        result = []

        for line in lines:
            m = re.match(regex, line)
            if m:
                result.append(m.group(1))

        return result
    except IOError:
        return None


def fetch_uniprotkb_file(id):
    content = requests.get("{}/{}.txt".format(const.UNIPROT_URL, id))
    
    if content.status_code != 200:
        return None
    return content.text
    
