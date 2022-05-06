from flask_restful import Resource
from flask import request
import json

from boomerang.data.validated import ValidatedDict
from boomerang.data.user import userDataHandle
from boomerang.data.music import raveUpDataHandle

class routeRaveUp():
    '''
    Class for routing all Rave Up data.
    '''

    class routeRaveUpBestRankings(Resource):
        def get(self, album_id):
            '''
            Route network rankings for album
            '''
            weeklyTop = []

            if album_id is None:
                return None

            index = 0
            for score in raveUpDataHandle.getRaveUpRanking(album_id):
                score: ValidatedDict = score
                scoredata = score.get_dict('data', {})
                user: ValidatedDict = userDataHandle.userFromUserID(score.get_int('userid'))

                weeklyTop.append(
                    {
                        'name': user.get_dict('data').get_str('name'),
                        'nation': 'KR',
                        'score': scoredata.get_int('score'),
                        'ranking': index
                    }
                )
                index += 1
                
            data = {
                'weeklyTop': weeklyTop
            }

            return data, 200

    class routeRaveUpUserRecord(Resource):
        def get(self, album_id, user_id):
            '''
            Load a user's score from a rave_up album
            '''
            album = raveUpDataHandle.getAlbum(int(user_id), album_id)
            if album is not None:
                data = album.get_dict('data')
            else:
                return {}, 200

            return {
                'best': {
                    'score': data.get_int('score'),
                    'maxCombo': data.get_int('maxCombo'),
                    'accuracy': data.get_int('totalAccuracy'),
                    'rankClass': data.get_str('rankClass')
                },
                'bestEmblem': data.get_dict('emblem')
            }, 200

    class routeRaveUpGuestRecord(Resource):
        def get(self, album_id):
            '''
            return nothing because guests deserve nothing
            '''
            return {}, 200

    class routeRaveUpSave(Resource):
        def post(self, user_id):
            '''
            Save the album data.
            '''
            sent = ValidatedDict(request.json)

            if sent.get_bool('cleared'):
                album_id = sent.get_str('albumId')
                game = sent.get_dict('game', {})
                played_songs = sent.get('playMusics')
                game.replace_str('playMusics', json.dumps(played_songs))
                user = userDataHandle.userFromUserID(int(user_id))

                # Save user data
                userdict = user.get_dict('data')
                userdict.replace_int('points', game.get_int('optainBeatPoint') + userdict.get_int('points'))
                userdict.replace_int('exp', game.get_int('optainExp') + userdict.get_int('exp'))
                user.replace_dict('data', userdict)
                userDataHandle.putUserFromUserID(user_id, user)

                # Save the album itself
                raveUpDataHandle.putAlbum(int(user_id), album_id, game)

            return 200

    class routeRaveUpSaveGuest(Resource):
        def post(self):
            return {}, 200

    class routeNearRaveUpRankings(Resource):
        def get(self, album_id):
            rankings = []
            index = 0

            for score in raveUpDataHandle.getRaveUpRanking(album_id):
                score: ValidatedDict = score
                scoredata = score.get_dict('data', {})
                user: ValidatedDict = userDataHandle.userFromUserID(score.get_int('userid'))

                rankings.append(
                    {
                        'name': user.get_dict('data').get_str('name'),
                        'nation': 'KR',
                        'score': scoredata.get_int('score'),
                        'ranking': index
                    }
                )
                index += 1

            return rankings, 200