from os.path import exists
import sqlite3

class setupDatabase():
    '''
    Class to verify that the DB is correct.
    Does simple checks.
    '''
    def checkForDB():
        '''
        Checks to see if the database file exists.
        '''
        database_exists = exists("./boomerang/db/database.sql")
        if database_exists:
            return True
        else: return False

    def createDatabase():
        '''
        Creates a database with all required tables.
        '''
        connection = sqlite3.connect('./boomerang/db/database.sql')

        tables = [
            "CREATE TABLE notice (id INTEGER PRIMARY KEY AUTOINCREMENT, nation TEXT, title TEXT, conenttype TEXT, content TEXT, content2 TEXT, image TEXT)",
            "CREATE TABLE machine (id INTEGER PRIMARY KEY AUTOINCREMENT, machineid TEXT)",
            "CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, cardid TEXT NOT NULL, banned bool NOT NULL, data TEXT NOT NULL)",
        ]

        for table in tables:
            print(table)
            cursor = connection.cursor()
            cursor.execute(table)

        connection.close()

    if checkForDB() == False:
        createDatabase()