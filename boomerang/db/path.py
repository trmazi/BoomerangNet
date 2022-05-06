import os

class SQLPath:
    def getSQLPath():
        return os.path.abspath(os.path.dirname(__file__)) + '/database.sql'