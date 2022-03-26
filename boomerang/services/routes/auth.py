from flask_restful import Resource
from flask import request

from boomerang.data.user import userDataHandle

class routeAuth():
    '''
    Class for routing all authentications.
    '''
    class noCardLogin(Resource):
        '''
        Handle the no cardid login.
        '''
        def post(self):
            return 200

    class login(Resource):
        '''
        Handle base login.
        '''
        def post(self):
            cardid = request.json['cardId']

            user, success = userDataHandle.userFromCardID(cardid)
            if not success:
                userdata = {
                    'authorization': '',
                    'userId': "NEWUSER",
                    'isSuccess': success,
                }
            else:
                if user.get('banned'):
                    return {
                        'authorization': '',
                        'userId': str(user.get('id')),
                        'isSuccess': False,
                    }, 200
                
                userdata = {
                    'authorization': '',
                    'userId': str(user.get('id')),
                    'isSuccess': success,
                }
            return userdata, 200