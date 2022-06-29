from flask_restful import Resource

class routeNetworkPatches():
    '''
    Class for handling all network patches.
    '''
    class routeUpdateVersion(Resource):
        '''
        Class for getting the current build of the game.
        '''
        def get(self):
            return 1