from flask_restful import Resource

from boomerang.data.network import networkDataHandle

class machineRoutes():
    '''
    A class used to route all of the main machine calls. 
    Will handle data such as machine points and more.
    '''
    class routeMachinePoints(Resource):
        def get(self, machine_id):
            if networkDataHandle.getMachineFromID(machine_id) == None:
                data = {
                    'point': 0
                }
            else:
                data = {
                    'point': 90
                }
            return data, 200