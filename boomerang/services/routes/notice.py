from flask_restful import Resource

from boomerang.data.network import networkDataHandle

class routeNotices(Resource):
    '''
    Class for handling newsposts.
    '''
    def get(self):
        data = {
            'notices': networkDataHandle.getAllNews()
        }

        return data, 200