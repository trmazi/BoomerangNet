from flask_restful import Resource

class routeBaseData():
    '''
    Class for routing base server data.
    '''
    class routeUserLevelTable(Resource):
        def get(self):
            '''
            For adjusting level up data. We're not messing with this for now.
            '''

            return None