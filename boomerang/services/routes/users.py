from flask_restful import Resource

class routeUsers():
    '''
    Class for handling user information.
    '''
    class routeUserGet(Resource):
        def get(self, user_id):
            if user_id is None:
                return None
            
            items = []

            userdata = {
                'userId': user_id,
                'nation': 'KR',
                'name': 'Trmazi',
                'iconId': 1039,
                'level': 5,
                'beatPoint': 500,
                'exp': 100,
                'userItems': items,
            }
            return userdata, 200

    class routeUserConfig(Resource):
        def post(self, user_id):
            return 200

    class routeGuestUserConfig(Resource):
        def post(self):
            return 200