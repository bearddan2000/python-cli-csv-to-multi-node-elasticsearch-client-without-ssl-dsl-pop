import os, csv
from database.schema import COLUMN_NAME

INDEX_NAME = os.environ["INDEX_NAME"]

def main():
    colums = [
        COLUMN_NAME['col_0']['name'],
        COLUMN_NAME['col_1']['name'],
        COLUMN_NAME['col_2']['name'],
        COLUMN_NAME['col_3']['name'],
        COLUMN_NAME['col_4']['name']
    ]    
    with open('{}.csv'.format(INDEX_NAME), "r") as fi:
        reader = csv.DictReader(
            fi, fieldnames=colums, delimiter=",", quotechar='"'
        )

        # This skips the first row which is the header of the CSV file.
        next(reader)

        actions = []
        for row in reader:
            split_field = row[COLUMN_NAME['col_2']['name']].split('::')
            csv_doc = {
                COLUMN_NAME['col_0']['name']: int(row[COLUMN_NAME['col_0']['name']]),
                COLUMN_NAME['col_1']['name']: row[COLUMN_NAME['col_1']['name']],
                COLUMN_NAME['col_2']['name']: split_field,
                COLUMN_NAME['col_3']['name']: float(row[COLUMN_NAME['col_3']['name']]),
                COLUMN_NAME['col_4']['name']: int(row[COLUMN_NAME['col_4']['name']])
            }
            actions.append(csv_doc)

        return actions

DOC = main()