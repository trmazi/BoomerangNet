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
            return missionDataHandle.getMission(int(user_id), mission_id).get_dict('data'), 200

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