from flask_restful import Resource, reqparse

class routeMusic():
    '''
    Class for handling all music requests
    '''
    class routeMusicBestRankings(Resource):
        def get(self, music_id, user_id):
            patternstatus = []
            weeklyTop = []

            if music_id is None:
                return None

            if user_id is not None:
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
            print(music_id)
            return [{}], 200