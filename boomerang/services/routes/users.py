from flask_restful import Resource

from boomerang.data.validated import ValidatedDict
from boomerang.data.user import userDataHandle

class routeUsers():
    '''
    Class for handling user information.
    '''
    class routeUserGet(Resource):
        def get(self, user_id):
            if user_id is None:
                return None

            user:ValidatedDict = userDataHandle.userFromUserID(int(user_id))
            userdict = user.get_dict('data')

            userdata = {
                'userId': user.get_int('id', None),
                'nation': userdict.get_str('nation', "KR"),
                'name': userdict.get_str('Name', "Guest"),
                'iconId': userdict.get_int('icon', 1000),
                'level': userdict.get_int('level', 1),
                'beatPoint': userdict.get_int('points'),
                'exp': userdict.get_int('exp'),
                'userItems': [],
            }
            return userdata, 200

    class routeUserConfig(Resource):
        def post(self, user_id):
            return 200

    class routeGuestUserConfig(Resource):
        def post(self):
            return 200