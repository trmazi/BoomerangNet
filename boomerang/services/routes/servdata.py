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

            def get_key(val, dict):
                for key, value in dict.items():
                    if val == value:
                        return key

            for i in range(1, 100):
                last = get_key(i-1, UserLevelTable.table)
                this = get_key(i, UserLevelTable.table)
                next = get_key(i+1 if i+1 <= 99 else 99, UserLevelTable.table)
                print (i, next)

                level = {
                    'level': i,
                    'levelUpExp': last,
                    'maxExp': next - this,
                }
                levellist.append(level)

            return levellist