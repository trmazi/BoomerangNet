from flask_restful import Resource

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