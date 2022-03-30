from flask_restful import Resource

from boomerang.data.music import scoreDataHandle
from boomerang.data.validated import ValidatedDict

class routeMusic():
    '''
    Class for handling all music requests
    '''
    class routeMusicBestRankings(Resource):
        '''
        Returns top ranking data and player's data for a song.
        '''
        def get(self, music_id, user_id):
            patternstatus = []
            weeklyTop = []

            if music_id is None:
                return None
            if user_id is not None:
                scores = scoreDataHandle.getScoreAllCharts(int(user_id), music_id)

                if scores is not None:
                    for score in scores:
                        score: ValidatedDict = score
                        scoredata = score.get_dict('data', {})
                        patternstatus.append(
                            {
                                'patternId': score.get_int('chart'),
                                'best':{
                                    'score': scoredata.get_int('score'),
                                    'noteScore': scoredata.get_int('noteScore'),
                                    'maxCombo': scoredata.get_int('maxCombo'),
                                    'realCombo': scoredata.get_int('realCombo'),
                                    'accuracy': scoredata.get_int('totalAccuracy'),
                                    'rankClass': scoredata.get_str('rankClass'),
                                },
                                'bestEmblem': scoredata.get_dict('emblem'),
                                'recently': [
                                    {'score': scoredata.get_int('score')},
                                ]
                            }
                        )

            # Network-wide rankings.
            for i in range(100):
                weeklyTop.append(
                    {
                        'name': 'JoeMama',
                        'nation': 'KR',
                        'score': 100*i,
                        'ranking': i
                    }
                )
                
            data = {
                'userPatternsStatus': patternstatus,
                'weeklyTop': weeklyTop
            }

            return data, 200

    class routeGuestMusicBestRankings(Resource):
        def get(self, music_id):
            patternstatus = []
            weeklyTop = []

            if music_id is None:
                return None

            # Route for guest
            patternstatus.append(
                {
                    'best':{
                        'score': 6969,
                        'noteScore': 100,
                        'maxCombo': 10,
                        'realCombo': 20,
                        'accuracy': 100,
                        'rankClass': 'A',
                    }
                }
            )

            for i in range(100):
                weeklyTop.append(
                    {
                        'name': 'JoeMama',
                        'nation': 'KR',
                        'score': 100*i,
                        'ranking': i
                    }
                )
                
            data = {
                'userPatternStatus': patternstatus,
                'weeklyTop': weeklyTop
            }

            return data, 200

    class routeNearRankings(Resource):
        def get(self, music_id):
            return [{}], 200