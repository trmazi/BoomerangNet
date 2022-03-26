from boomerang.data.sql import coreSQL

class userDataHandle():
    '''
    Handler for reacting to userdata.
    '''

    def userFromCardID(cardid: str):
        '''
        Gets a user's cardID, returns user's profile and success bool.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM user where cardid= '{cardid}'")

        result = cursor.fetchone()

        if result is None:
            return ({}, False)
        else:
            userid, card, banned, data = result
            return (
                {
                    'id': userid,
                    'cardid': card,
                    'banned': banned,
                    'data': data
                },
                True
            )