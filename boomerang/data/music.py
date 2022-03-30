import json

from boomerang.data.sql import coreSQL
from boomerang.data.validated import ValidatedDict

class scoreDataHandle():
    '''
    Class for dealing with scores.
    '''

    def putScore(userid: int, songid: str, chart: int, scoredata: ValidatedDict):
        '''
        Given a userid, songid, and a score, saves it.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()

        # Figure out if we've already done better on this song+chart
        oldscore = scoreDataHandle.getScore(userid, songid, chart)
        olddata = ValidatedDict({})
        if oldscore != None:
            olddata = oldscore.get_dict('data', {})
        if olddata.get_int('totalAccuracy') > scoredata.get_int('totalAccuracy') and olddata.get_int('score') > scoredata.get_int('score'):
            cursor.execute(f"UPDATE score SET userid={userid}, musicid='{songid}', chart={chart}, data='{json.dumps(olddata)}'")
        else:
            cursor.execute(f"INSERT INTO score (userid, musicid, chart, data) VALUES ({userid}, '{songid}', {chart}, '{json.dumps(scoredata)}')")
        
        connection.commit()
        connection.close()

    def getScore(userid: int, songid: str, chart: int):
        '''
        Given the userid, songid, and chart of a score, returns said score.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM score where userid={userid} and musicid='{songid}' and chart={chart}")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            scoreid, userid, songid, chart, data = result
            connection.close()
            return ValidatedDict({
                'id': scoreid,
                'userid': userid,
                'songid': songid,
                'chart': chart,
                'data': json.loads(data)
            })

    def getScoreAllCharts(userid: int, songid: str):
        '''
        Given the userid and songid of a score, returns array of all scores.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM score where userid={userid} and musicid='{songid}'")

        results = cursor.fetchall()

        if results is None:
            connection.close()
            return None
        else:
            scores = []
            for result in results:
                scoreid, userid, songid, chart, data = result
                connection.close()
                scores.append(ValidatedDict({
                    'id': scoreid,
                    'userid': userid,
                    'songid': songid,
                    'chart': chart,
                    'data': json.loads(data)
                }))
            return scores