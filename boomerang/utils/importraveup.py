import argparse
import sqlite3
import os
import sys
import json

import boomerang.data.sql

def importFunctions(db, csv):
    '''
    Main Function for imports
    '''
    def prepareForImport(db, csv):
        '''
        Verifies that the DB exists, if not, calls to make it.
        '''
        if not os.path.exists(db):
            boomerang.data.sql.setupDatabase

        if not os.path.exists(csv):
            sys.exit("Your CSV doesn't actually exist! Please supply a proper CSV.")
        
    def pullDataFromCSV(csv):
        '''
        Reads through the CSV file and pulls all relevant data
        '''
        file = open(csv, 'rb')
        data = file.read().decode('utf-8')

        sets = []

        for entry in data.split('\n'):
            entrylist = entry.split(',')
            if 'id' in entrylist[0]:
                continue
            if entrylist[0] == '':
                continue

            set = {
                'albumid': entrylist[5],
                'title': entrylist[2],
                'data': {
                    'discstock': entrylist[1],
                    'difficulty': entrylist[4],
                    'subtext': entrylist[3],
                }
            }
            sets.append(set)
        return sets

    def importToDB(sets: list, db):
        '''
        Take the sets object, import it to the DB
        '''
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        index = 0

        for set in sets:
            set:dict = set

            print(f"Importing data for {set.get('title')}")
            data = json.dumps(set.get('data'))
            songlist = (index, set.get('albumid'), set.get('title'), data)
            cursor.execute("INSERT INTO rave_up VALUES (?, ?, ?, ?)", songlist)
            index += 1

        connection.commit()
        connection.close()

        print("Done importing!")

    prepareForImport(db, csv)
    data = pullDataFromCSV(csv)
    importToDB(data, db)

def main() -> None:
    parser = argparse.ArgumentParser(description="Song import tool. Reads the game's DB, imports it.")
    parser.add_argument("--csv", help="The DiscStock.csv file", type=str, required=True)
    parser.add_argument('--db', help="Specify the location of the DB. Has default path.", type=str, default='./boomerang/db/database.sql')
    args = parser.parse_args()

    # start the sequence
    importFunctions(args.db, args.csv)

if __name__ == '__main__':
    main()