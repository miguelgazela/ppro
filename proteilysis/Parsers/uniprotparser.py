import re

class UniprotParser(object):
    """
    
    """

    def __init__(self, structureID, content=''):
        self.content = content
        self.structureID = structureID
        self.helices_records = []
        self.sheets_records = []
        self.sequence_records = []
        self.title = []

        lines = content.splitlines()

        for line in lines:
            line = line.strip()

            if re.search('^HEADER', line):
                self.classification = line[10:50]
            elif re.search('^TITLE', line):
                self._parse_title(line)
            elif re.search('^HELIX', line):
                self.helices_records.append(line)
            elif re.search('^SHEET', line):
                self.sheets_records.append(line)
            elif re.search('^SEQRES', line):
                self.sequence_records.append(line)

        self.title = "".join(self.title)

        self._build_helices()
        self._build_sheets()
        self._build_sequence()

    def _parse_title(self, line):
        pass
