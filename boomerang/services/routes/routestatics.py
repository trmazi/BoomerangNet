from flask_restful import Resource
import os

from boomerang.services.static.path import StaticPath

class routeStatics():
    '''
    Class for handling the routing of static files.
    These are usually calling for .txt files.
    '''
    class routeEmergency(Resource):
        def get(self):
            emergencydata = open(os.path.abspath(StaticPath.getStaticPath()+'/Emergency.txt'), 'rb')
            emergencytxt = emergencydata.read().decode('utf-8')
            emergencydata.close()
            return emergencytxt

    class routeNewSongEvent(Resource):
        def get(self):
            nsedata = open(os.path.abspath(StaticPath.getStaticPath()+'/newsongevent.txt'), 'rb')
            nsetxt = nsedata.read().decode('utf-8')
            nsedata.close()
            return nsetxt