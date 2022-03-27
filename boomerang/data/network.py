from boomerang.data.sql import coreSQL
from boomerang.data.validated import ValidatedDict

class networkDataHandle():
    '''
    Handle core network data.
    '''

    def getMachineFromID(machine_id: str):
        '''
        Given a Machine ID, return a machine dict.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM machine where machineid= '{machine_id}'")

        result = cursor.fetchone()

        if result is None:
            connection.close()
            return None
        else:
            id, machineid, arcade = result
            connection.close()
            return ValidatedDict({
                    'id': id,
                    'machineid': machineid,
                    'arcade': arcade,
                }
            )