import requests
from constants import BASE_URL, NO_SUCH_FILE_URL

def fetch_pdb_file(id):
    """
    Returns the content of a pdb file if it exists or None if it doesn't
    """
    content = requests.get("%s/%s.pdb" % (BASE_URL, id))
    
    if not content.url == NO_SUCH_FILE_URL:
        return content.text
    return None


    
