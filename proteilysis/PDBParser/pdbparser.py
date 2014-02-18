class PDBParser(object):
    """
    Class responsible for parsing the content of a pdb file.
    In the end it holds the helices, sheets and aminoacid sequence of
    the received structure.
    """

    def __init__(self, content=''):
        self.content = content
        self.helices_records = []
        self.sheets_records = []

        lines = content.splitlines()

        for line in lines:
            line = line.strip()
            record_name = line[0:5]

            if record_name == 'HELIX':
                self.helices_records.append(line)
            elif record_name == 'SHEET':
                self.sheets_records.append(line) 

        self._build_helices()
        self._build_sheets()


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

            helixID = record[11:14]
            initResName = record[15:18]
            initChainID = record[19]
            initSeqNum = int(record[21:25])
            initICode = record[25]
            endResName = record[27:30]
            endChainID = record[31]
            endSeqNum = int(record[33:37])
            endICode = record[37]
            helixClass = int(record[38:40])
            comment = record[40:70]
            length = int(record[71:76])

            helix = Helix(serNum, helixID, initResName, initChainID,
                initSeqNum, initICode, endResName, endChainID,
                endSeqNum, endICode, helixClass, comment, length)
            self.helices.append(helix)


    def _build_sheets(self):
        """
        Parses the sheets records and builds the Sheets objects
        """
        self.sheets = []

        for record in self.sheets_records:
            strand = int(record[7:10])
            sheetID = record[11:14]
            numStrands = int(record[14:16])
            initResName = record[17:20]
            initChainID = record[21]
            initSeqNum = int(record[22:26])
            initICode = record[26]
            endResName = record[28:31]
            endChainID = record[32]
            endSeqNum = int(record[33:37])
            endICode = record[37]
            sense = int(record[38:40])

            if sense != 0:
                curAtom = record[41:45]
                curResName = record[45:48]
                curChainID = record[49]
                curResSeq = int(record[50:54])
                curICode = record[54]
                prevAtom = record[56:60]
                prevResName = record[60:63]
                prevChainID = record[64]
                prevResSeq = int(record[65:69])
                # prevICode = record[69]
                prevICode = "" # TODO

                sheet = Sheet(strand, sheetID, numStrands, initResName,
                    initChainID, initSeqNum, initICode, endResName, endChainID,
                    endSeqNum, endICode, sense, curAtom, curResName, curChainID, 
                    curResSeq, curICode, prevAtom, prevResName, prevChainID, 
                    prevResSeq, prevICode)
            else:
                sheet = Sheet(strand, sheetID, numStrands, initResName,
                    initChainID, initSeqNum, initICode, endResName, endChainID,
                    endSeqNum, endICode, sense)

            self.sheets.append(sheet)



class Helix(object):
    """
    Represents a helix record of the pdb file
    """

    def __init__(self, serNum, helixID, initResName, initChainID, initSeqNum, 
            initICode, endResName, endChainID, endSeqNum, endICode, helixClass,
            comment, length):
        self.serNum = serNum
        self.helixID = helixID
        self.initResName = initResName
        self.initChainID = initChainID
        self.initSeqNum = initSeqNum
        self.initICode = initICode
        self.endResName = endResName
        self.endChainID = endChainID
        self.endSeqNum = endSeqNum
        self.endICode = endICode
        self.helixClass = helixClass
        self.comment = comment
        self.length = length

class Sheet(object):
    """
    Represents a sheet record of the pdb file
    """

    def __init__(self, strand, sheetID, numStrands, initResName, initChainID,
            initSeqNum, initICode, endResName, endChainID, endSeqNum, endICode,
            sense, curAtom="", curResName="", curChainID="", curResSeq="",
            curICode="", prevAtom="", prevResName="", prevChainID="",
            prevResSeq="", prevICode=""):
        self.strand = strand
        self.sheetID = sheetID
        self.numStrands = numStrands
        self.initResName = initResName
        self.initChainID = initChainID
        self.initSeqNum = initSeqNum
        self.initICode = initICode
        self.endResName = endResName
        self.endChainID = endChainID
        self.endSeqNum = endSeqNum
        self.endICode = endICode
        self.prevResName = prevResName
        self.prevChainID = prevChainID
        self.prevResSeq = prevResSeq
        self.prevICode = prevICode