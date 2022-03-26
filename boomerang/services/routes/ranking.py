from flask_restful import Resource

class routeRanking():
    '''
    Class for handling all ranking data
    '''
    class bootupRanking(Resource):
        '''
        I don't actually know how to handle this request lol, it's weird.
        '''
        def get(self):
            return {}, 200