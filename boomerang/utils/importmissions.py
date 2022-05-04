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

        missions = []

        for entry in data.split('\n'):
            entrylist = entry.split(',')
            if 'MissionType' in entrylist[0]:
                continue
            if entrylist[0] == '':
                continue

            mission = {
                'gameid': entrylist[39],
                'difficulty': int(entrylist[5]),
                'm_title': entrylist[4],
                'p_title': entrylist[2],
                'data': {
                }
            }
            missions.append(mission)
        return missions

    def importToDB(missions: list, db):
        '''
        Take the missions object, import it to the DB
        '''
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        index = 0
        for song in missions:
            song:dict = song

            print(f"Importing data for {song.get('m_title')}")
            data = json.dumps(song.get('data'))
            songlist = (index, song.get('gameid'), song.get('difficulty'), song.get('m_title'), song.get('p_title'), data)
            cursor.execute("INSERT INTO mission VALUES (?, ?, ?, ?, ?, ?)", songlist)
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