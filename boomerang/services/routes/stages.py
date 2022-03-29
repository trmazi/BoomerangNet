from flask_restful import Resource
from flask import request

from boomerang.data.validated import ValidatedDict
from boomerang.data.user import userDataHandle

class routeStages():
    '''
    Class for routing all stage data.
    This is used for saving scores.
    '''
    class routeUserMusicHistories(Resource):
        def post(self, user_id):
            return 200

    class routeUserFinalHistories(Resource):
        '''
        This is actually where the end-game data is saved,
        such as XP and BP. Keeping it in stages though, as that's 
        how it's sent.
        '''

        def post(self, user_id):
            sent = ValidatedDict(request.json)
            print(request.json)
            user = userDataHandle.userFromUserID(int(user_id))
            userdict = user.get_dict('data')

            userdict.replace_int('points', sent.get_int('optainBeatPoint') + userdict.get_int('points'))
            userdict.replace_int('exp', sent.get_int('optainExp') + userdict.get_int('exp'))

            user.replace_dict('data', userdict)
            userDataHandle.putUserFromUserID(user_id, user)
            return 200

    class routeGuestUserMusicHistories(Resource):
        def post(self):
            return 200

    class routeGuestUserFinalHistories(Resource):
        def post(self):
            return 200

    class routeStageNearRankings(Resource):
        def get(self):
            return 200