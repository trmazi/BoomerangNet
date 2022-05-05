from flask_restful import Resource
from flask import request

from boomerang.data.music import missionDataHandle
from boomerang.data.validated import ValidatedDict
from boomerang.data.user import userDataHandle

class routeMission():
    '''
    Class for routing all mission data.
    '''
    class routeMissionLoad(Resource):
        def get(self, mission_id, user_id):
            '''
            Load score for mission.
            '''
            mission = missionDataHandle.getMission(int(user_id), mission_id)
            if mission is not None:
                data = mission.get_dict('data')
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

    class routeMissionLoadGuest(Resource):
        def get(self):
            return {}

    class routeMissionSave(Resource):
        def post(self, user_id):
            '''
            Save the mission data.
            '''
            sent = ValidatedDict(request.json)

            if sent.get_bool('conditionCleared'):
                mission_id = sent.get_str('missionId')
                game = sent.get_dict('game', {})
                user = userDataHandle.userFromUserID(int(user_id))

                # Save user data
                userdict = user.get_dict('data')
                userdict.replace_int('points', game.get_int('optainBeatPoint') + userdict.get_int('points'))
                userdict.replace_int('exp', game.get_int('optainExp') + userdict.get_int('exp'))
                user.replace_dict('data', userdict)
                userDataHandle.putUserFromUserID(user_id, user)

                # Save the mission itself
                missionDataHandle.putMission(int(user_id), mission_id, game)

            return 200

    class routeMissionSaveGuest(Resource):
        def post(self):
            return 201

    class routeNearMissionRankings(Resource):
        def get(self, mission_id):
            rankings = []
            index = 0

            for score in missionDataHandle.getMissionRanking(mission_id):
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