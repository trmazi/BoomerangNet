from flask_restful import Resource

class routeRanking():
    '''
    Class for handling all ranking data
    '''
    class bootupRanking(Resource):
        '''
        Demo loop ranking data
        '''
        def get(self):
            return {}, 200