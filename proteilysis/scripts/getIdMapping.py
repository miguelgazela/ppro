#!/usr/bin/env python

import requests
from sys import argv

content = requests.get("http://www.uniprot.org/mapping/",
        params={'from': 'PDB_ID', 'to': 'ACC', 'format': 'tab', 'query': argv[1]})
    
content = content.text.split()

if content[-1] != 'To':
	print content[-1]
else:
	print ""
