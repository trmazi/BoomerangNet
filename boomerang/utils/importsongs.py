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

        songs = []

        for entry in data.split('\n'):
            entrylist = entry.split(',')
            if entrylist[0] == 'id':
                continue
            if entrylist[0] == '':
                continue

            song = {
                'id': int(entrylist[0]),
                'title': entrylist[2],
                'artist': entrylist[9],
                'difficulty': int(entrylist[4]),
                'genre': entrylist[3],
                'gameid': str(entrylist[11]),
                'data': {
                    'bpm': int(entrylist[5]),
                    'composer': entrylist[6],
                    'vocalist': entrylist[8],
                    'charts': entrylist[10].split("_"),
                }
            }
            songs.append(song)
        return songs

    def importToDB(songs: list, db):
        '''
        Take the songs object, import it to the DB
        '''
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        for song in songs:
            song:dict = song

            print(f"Importing data for {song.get('title')}")
            data = json.dumps(song.get('data'))
            songlist = (song.get('id'), song.get('gameid'), song.get('difficulty'), song.get('title'), song.get('artist'), song.get('genre'), data)
            cursor.execute("INSERT INTO music VALUES (?, ?, ?, ?, ?, ?, ?)", songlist)

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