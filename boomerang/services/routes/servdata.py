from flask_restful import Resource

class routeBaseData():
    '''
    Class for routing base server data.
    '''
    class routeUserLevelTable(Resource):
        def get(self):
            levellist = []

            for i in range (15):
                leveltable = {
                    'level': i,
                    'levelUpExp': 10,
                    'maxExp': 100*i,
                }
                levellist.append(leveltable)

            return levellist