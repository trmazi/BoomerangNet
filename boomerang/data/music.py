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

        # Figure out if we've already done better on this song+chart
        oldscore = scoreDataHandle.getScore(userid, songid, chart)
        if oldscore != None:
            olddata = oldscore.get_dict('data', {})
            if olddata.get_int('totalAccuracy') > scoredata.get_int('totalAccuracy') and olddata.get_int('score') > scoredata.get_int('score'):
                scoredata = olddata

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE score SET userid={userid}, musicid='{songid}', chart={chart}, data='{json.dumps(scoredata)}'")
        connection.commit()
        connection.close()

    def getScore(userid: int, songid: str, chart: int):
        '''
        Given the userid, songid, and chart of a score, returns said score.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM score where userid={userid}, musicid='{songid}', chart={chart}")

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