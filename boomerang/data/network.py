from boomerang.data.sql import coreSQL
from boomerang.data.validated import ValidatedDict
import os

from boomerang.web.assets.profileicn.path import IconPath

class networkDataHandle():
    '''
    Handle core network data.
    '''

    def getIconList():
        '''
        Returns a list of tupeles with data of (id, filename)
        '''
        iconlist = []
        for icon in os.listdir(IconPath.getIconPath()):
            iconlist.append((int(icon.replace('.png', '')), icon))

        return iconlist

    def getAllNews():
        '''
        Returns all news from the server.
        '''
        connection = coreSQL.makeConnection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM notice ORDER BY id DESC")

        results = cursor.fetchall()
        if results == None:
            return None

        allnews = []
        
        for result in results:
            newsid, nation, title, contenttype, content, content2, image = result
            allnews.append(ValidatedDict(
                {
                    'noticeNo': newsid-1+1000,
                    'nation': nation,
                    'title': title,
                    'noticeType': 'event',
                    'contentType': contenttype,
                    'content': content,
                    'content2': content2,
                    'image': image
                }
            ))

        return allnews

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