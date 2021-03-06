import json

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
                    'data': json.loads(data)
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
                'data': json.loads(data)
            })

    def checkForCardid(cardid: str):
        '''
        Given a cardid, return a bool if it's there or not.
        '''

        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM user where cardid= '{cardid}'")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return False
        else:
            connection.close()
            return True

    def putUserFromUserID(userid: int, user: ValidatedDict):
        '''
        Given a valid user dict, put it in the server.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE user SET cardid='{user.get_str('cardid')}', data='{json.dumps(user.get_dict('data'))}' WHERE id={user.get_int('id')}")
        connection.commit()
        connection.close()

    def createNewUser(user: ValidatedDict):
        '''
        Given a valid user dict, put it in the server.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO user (cardid, data, banned) VALUES ('{user.get_str('cardid')}', '{json.dumps(user.get_dict('data'))}', 0)")
        connection.commit()
        connection.close()