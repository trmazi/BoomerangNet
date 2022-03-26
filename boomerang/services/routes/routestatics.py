from flask_restful import Resource
import os

class routeStatics():
    '''
    Class for handling the routing of static files.
    These are usually calling for .txt files.
    '''
    class routeEmergency(Resource):
        def get(self):
            emergencydata = open(os.path.abspath('./boomerang/services/static/Emergency.txt'), 'rb')
            emergencytxt = emergencydata.read().decode('utf-8')
            emergencydata.close()
            return emergencytxt

    class routeNewSongEvent(Resource):
        def get(self):
            nsedata = open(os.path.abspath('./boomerang/services/static/newsongevent.txt'), 'rb')
            nsetxt = nsedata.read().decode('utf-8')
            nsedata.close()
            return nsetxt