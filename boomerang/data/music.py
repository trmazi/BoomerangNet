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
            oldid = oldscore.get_int('id')
            if olddata.get_int('totalAccuracy') < scoredata.get_int('totalAccuracy') and olddata.get_int('score') < scoredata.get_int('score'):
                cursor.execute(f"UPDATE score SET data='{json.dumps(olddata)}' where userid={userid} and musicid='{songid}' and chart={chart} and id={oldid}")
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

    def getScoreRanking(songid: str):
        '''
        Given the songid of a score, returns array of all scores.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM score where musicid='{songid}'")

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

    def getAllScores():
        '''
        Returns a list of all the scores on the network
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM score ORDER BY id DESC")

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

class missionDataHandle():
    def putMission(userid: int, missionid: str, scoredata: ValidatedDict):
        '''
        Given a userid, missionid, and a score, saves it.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()

        # Figure out if we've already done better on this mission
        oldscore = missionDataHandle.getMission(userid, missionid)
        olddata = ValidatedDict({})
        if oldscore != None:
            olddata = oldscore.get_dict('data', {})
            oldid = oldscore.get_int('id')

            if olddata.get_int('totalAccuracy') < scoredata.get_int('totalAccuracy') and olddata.get_int('score') < scoredata.get_int('score'):
                cursor.execute(f"UPDATE mission_score SET data='{json.dumps(olddata)}' where userid={userid} and missionid='{missionid}' and id={oldid}")
        else: 
            cursor.execute(f"INSERT INTO mission_score (userid, missionid, data) VALUES ({userid}, '{missionid}', '{json.dumps(scoredata)}')")
        
        connection.commit()
        connection.close()

    def getMission(userid: int, missionid: str):
        '''
        Given the userid, missionid, returns said score.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM mission_score where userid={userid} and missionid='{missionid}'")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            scoreid, userid, missionid, data = result
            connection.close()
            return ValidatedDict({
                'id': scoreid,
                'userid': userid,
                'missionid': missionid,
                'data': json.loads(data)
            })

    def getAllMissions():
        '''
        Returns a list of all the missions on the network
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM mission_score ORDER BY id DESC")

        results = cursor.fetchall()

        if results is None:
            connection.close()
            return None
        else:
            scores = []
            for result in results:
                scoreid, userid, songid, data = result
                connection.close()
                scores.append(ValidatedDict({
                    'id': scoreid,
                    'userid': userid,
                    'missionid': songid,
                    'data': json.loads(data)
                }))
            return scores

    def getMissionRanking(missionid: str):
        '''
        Given the missionid of a mission, returns array of all scores.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM mission_score where missionid='{missionid}'")

        results = cursor.fetchall()

        if results is None:
            connection.close()
            return None
        else:
            scores = []
            for result in results:
                scoreid, userid, songid, data = result
                connection.close()
                scores.append(ValidatedDict({
                    'id': scoreid,
                    'userid': userid,
                    'missionid': songid,
                    'data': json.loads(data)
                }))
            return scores

class raveUpDataHandle():
    def putAlbum(userid: int, albumid: str, scoredata: ValidatedDict):
        '''
        Given a userid, albumid, and a score, saves it.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()

        # Figure out if we've already done better on this raveup
        oldscore = raveUpDataHandle.getAlbum(userid, albumid)
        olddata = ValidatedDict({})
        if oldscore != None:
            olddata = oldscore.get_dict('data', {})
            oldid = oldscore.get_int('id')

            if olddata.get_int('totalAccuracy') < scoredata.get_int('totalAccuracy') and olddata.get_int('score') < scoredata.get_int('score'):
                cursor.execute(f"UPDATE rave_score SET data='{json.dumps(olddata)}' where userid={userid} and albumid='{albumid}' and id={oldid}")
        else: 
            cursor.execute(f"INSERT INTO rave_score (userid, albumid, data) VALUES ({userid}, '{albumid}', '{json.dumps(scoredata)}')")
        
        connection.commit()
        connection.close()

    def getAlbum(userid: int, albumid: str):
        '''
        Given the userid, albumid, returns said score.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM rave_score where userid={userid} and albumid='{albumid}'")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            scoreid, userid, albumid, data = result
            connection.close()
            return ValidatedDict({
                'id': scoreid,
                'userid': userid,
                'albumid': albumid,
                'data': json.loads(data)
            })

    def getAllAlbums():
        '''
        Returns a list of all the albums on the network
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM rave_score ORDER BY id DESC")

        results = cursor.fetchall()

        if results is None:
            connection.close()
            return None
        else:
            scores = []
            for result in results:
                scoreid, userid, songid, data = result
                connection.close()
                scores.append(ValidatedDict({
                    'id': scoreid,
                    'userid': userid,
                    'albumid': songid,
                    'data': json.loads(data)
                }))
            return scores

    def getRaveUpRanking(albumid: str):
        '''
        Given the albumid of an album, returns array of all scores.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM rave_score where albumid='{albumid}'")

        results = cursor.fetchall()

        if results is None:
            connection.close()
            return None
        else:
            scores = []
            for result in results:
                scoreid, userid, albumid, data = result
                connection.close()
                scores.append(ValidatedDict({
                    'id': scoreid,
                    'userid': userid,
                    'albumid': albumid,
                    'data': json.loads(data)
                }))
            return scores

class songDataHandle():
    '''
    Class for getting information about songs.
    '''
    def getSongFromId(songid):
        '''
        Given a songid, return a song.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM music where gameid='{songid}'")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            id, gameid, difficulty, title, artist, genre, data = result
            connection.close()
            return ValidatedDict({
                'id': id,
                'gameid': gameid,
                'difficulty': difficulty,
                'title': title,
                'artist': artist,
                'genre': genre,
                'data': json.loads(data)
            })