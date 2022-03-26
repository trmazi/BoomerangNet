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