import re


class PDBParser(object):
    """
    Class responsible for parsing the content of a pdb file.
    In the end it holds the helices, sheets and aminoacid sequence of
    the received structure.
    """

    def __init__(self, structureID, content=''):
        self.content = content
        self.structureID = structureID
        self.helices_records = []
        self.sheets_records = []
        self.sequence_records = []

        lines = content.splitlines()

        for line in lines:
            line = line.strip()

            if re.search('^HELIX', line):
                self.helices_records.append(line)
            elif re.search('^SHEET', line):
                self.sheets_records.append(line)
            elif re.search('^SEQRES', line):
                self.sequence_records.append(line)

        self._build_helices()
        self._build_sheets()
        self._build_sequence()


    def _build_helices(self):
        """
        Parses the helices records and builds the Helices objects
        """
        self.helices = []
        inc = 1

        for record in self.helices_records:
            serNum = int(record[7:10])

            # check if the sequence of helices is right
            if serNum != inc:
                raise Exception
            inc += 1

            helix = {
                'structureID': self.structureID,
                'serNum': serNum,
                'helixID': record[11:14],
                'initResName': record[15:18],
                'initChainID': record[19],
                'initSeqNum': int(record[21:25]),
                'initICode': record[25],
                'endResName': record[27:30],
                'endChainID': record[31],
                'endSeqNum': int(record[33:37]),
                'endICode': record[37],
                'helixClass': int(record[38:40]),
                'comment': record[40:70],
                'length': int(record[71:76])
            }
            self.helices.append(helix)


    def _build_sequence(self):
        """
        Parses the sequence records and builds a Sequence object
        """
        self.sequence = []
        INITIAL_COLUMN = 19
        FINAL_COLUMN = 22

        for record in self.sequence_records:
            serNum = int(record[7:10])
            chainID = record[11]
            numRes = int(record[13:17])

            if numRes <= 13:
                rec_residues = numRes
            elif serNum == 1:
                rec_residues = 13
            else:
                read = 13 * (serNum - 1)
                rec_residues = (numRes - read <= 13) and (numRes - read) or 13

            residues = []
            for i in range(rec_residues):
                residues.append(
                    record[(INITIAL_COLUMN + 4 * i):(FINAL_COLUMN + 4 * i)])

            seq = {
                'serNum': serNum, 'chainID': chainID,
                'numRes': numRes, 'residues': residues,
                'structureID': self.structureID
            }
            self.sequence.append(seq)

    def _build_sheets(self):
        """
        Parses the sheets records and builds the Sheets objects
        """
        self.sheets = []

        for record in self.sheets_records:

            sheet  = {
                'structureID': self.structureID,
                'strand': int(record[7:10]),
                'sheetID': record[11:14],
                'numStrands': int(record[14:16]),
                'initResName': record[17:20],
                'initChainID': record[21],
                'initSeqNum': int(record[22:26]),
                'initICode': record[26],
                'endResName': record[28:31],
                'endChainID': record[32],
                'endSeqNum': int(record[33:37]),
                'endICode': record[37],
                'sense': int(record[38:40]),
            }
            
            if sheet['sense'] != 0:
                sheet['curAtom'] = record[41:45]
                sheet['curResName'] = record[45:48]
                sheet['curChainID'] = record[49]
                sheet['curResSeq'] = int(record[50:54])
                sheet['curICode'] = record[54]
                sheet['prevAtom'] = record[56:60]
                sheet['prevResName'] = record[60:63]
                sheet['prevChainID'] = record[64]
                sheet['prevResSeq'] = int(record[65:69])
                try:
                    sheet['prevICode'] = record[69]
                except IndexError:
                    sheet['prevICode'] = ''

            self.sheets.append(sheet)
