from flask_restful import Resource

from boomerang.data.validated import UserLevelTable

class routeBaseData():
    '''
    Class for routing base server data.
    '''
    class routeUserLevelTable(Resource):
        def get(self):
            '''
            For adjusting level up data.
            '''
            levellist = []

            for i in range(99):
                level = {
                    'level': i+1,
                    'levelUpExp': UserLevelTable.table.get(i),
                    'maxExp': UserLevelTable.table.get(i+1 if i != 99 else 99)
                }
                levellist.append(level)

            return levellist