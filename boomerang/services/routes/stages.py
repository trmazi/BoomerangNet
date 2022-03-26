from flask_restful import Resource

class routeStages():
    '''
    Class for routing all stage data.
    This is used for saving scores.
    '''
    class routeUserMusicHistories(Resource):
        def post(self, user_id):
            return 200

    class routeUserFinalHistories(Resource):
        def post(self, user_id):
            return 200

    class routeGuestUserMusicHistories(Resource):
        def post(self):
            return 200

    class routeGuestUserFinalHistories(Resource):
        def post(self):
            return 200

    class routeStageNearRankings(Resource):
        def post(self):
            return 200