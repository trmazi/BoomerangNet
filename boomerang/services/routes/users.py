from flask_restful import Resource

class routeUsers():
    '''
    Class for handling user information.
    '''
    class routeUserGet(Resource):
        def get(self, user_id):
            if user_id is None:
                return None
            
            userdata = {
                'userId': user_id,
                'nation': 'KR',
                'name': 'Trmazi',
                'icon': '',
                'iconId': 1,
                'level': 69,
                'beatPoint': 500,
                'exp': 1000,
                'userItems': [{}],
            }
            return userdata, 200

    class routeUserConfig(Resource):
        def post(self, user_id):
            return 200

    class routeGuestUserConfig(Resource):
        def post(self):
            return 200