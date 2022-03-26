from flask_restful import Resource
from flask import request

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

            userdata = {
                'authorization': '',
                'userId': cardid,
                'isSuccess': True,
            }
            return userdata, 200