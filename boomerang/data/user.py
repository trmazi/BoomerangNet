from boomerang.data.sql import coreSQL
from boomerang.data.validated import ValidatedDict

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
            connection.close()
            return ({}, False)
        else:
            userid, card, banned, data = result
            connection.close()
            return (
                ValidatedDict({
                    'id': userid,
                    'cardid': card,
                    'banned': banned,
                    'data': data
                }),
                True
            )

    def userFromUserID(userid: int):
        '''
        Gets a user's userID, returns user's profile.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM user where id= {userid}")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            userid, card, banned, data = result
            connection.close()
            return ValidatedDict({
                'id': userid,
                'cardid': card,
                'banned': banned,
                'data': data
            })