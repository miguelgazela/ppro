#!/usr/bin/env python

import os
import config


def main():
    with open(config.FILENAMES['PROTEINS_SQL'], 'w') as sql_file:
        for root, dirs, files in os.walk(config.PATHS['PDB_FILE_DIR']):
            for filename in files:
                sql_file.write(config.SQL_TEMPLATES['INSERT_PROTEIN'].format(
                    filename,
                    os.path.join(config.PATHS['PDB_FILE_DIR'], filename))
                )


if __name__ == "__main__":
    main()