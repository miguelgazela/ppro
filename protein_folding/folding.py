from PDBParser import PDBParser
from PDBParser import utils


def main():
    gtpase_kras = utils.fetch_pdb_file('3GFT')
    parser = PDBParser(gtpase_kras)

    for helice in parser.helices:
        print helice.helixClass

    for sheet in parser.sheets:
        print sheet.strand


if __name__ == "__main__":
    main()