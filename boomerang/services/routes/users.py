from flask_restful import Resource
from flask import request

from boomerang.data.validated import ValidatedDict, UserLevelTable
from boomerang.data.user import userDataHandle

class routeUsers():
    '''
    Class for handling user information.
    '''
    class routeUserGet(Resource):
        def get(self, user_id):
            if user_id is None:
                return None

            user = userDataHandle.userFromUserID(int(user_id))
            userdict = user.get_dict('data')
            configdict = userdict.get_dict('config')

            userlevel = UserLevelTable.table.get(userdict.get_int('exp')) or UserLevelTable.table[min(UserLevelTable.table.keys(), key = lambda key: abs(key-userdict.get_int('exp')))]

            userdata = {
                'userId': user.get_int('id', None),
                'nation': userdict.get_str('nation', "KR"),
                'name': userdict.get_str('name', "Newcomer"),
                'iconId': userdict.get_int('iconid', 1)+999,
                'level': userlevel,
                'beatPoint': userdict.get_int('points'),
                'exp': userdict.get_int('exp'),
                'configurations': configdict,
            }
            return userdata, 200

    class routeUserConfig(Resource):
        def post(self, user_id):
            user = userDataHandle.userFromUserID(int(user_id))
            userdict = user.get_dict('data')

            config = userdict.get_dict('config', {})
            sent = ValidatedDict(request.json)
            config.replace_str('IsUseKeySound', sent.get_str('IsUseKeySound'))
            config.replace_int('KeyEFfect', sent.get_int('KeyEFfect', 1))
            config.replace_str('KeyVolume', sent.get_str('KeyVolume'))
            config.replace_str('Speed', sent.get_str('Speed'))

            userdict.replace_dict('config', config)
            user.replace_dict('data', userdict)

            userDataHandle.putUserFromUserID(user_id, user)

            return 200

    class routeGuestUserConfig(Resource):
        def post(self):
            return 200