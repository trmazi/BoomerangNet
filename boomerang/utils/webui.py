from flask import Flask, render_template, request, url_for, send_from_directory
import random
import string

from boomerang.data.user import userDataHandle
from boomerang.data.music import scoreDataHandle, songDataHandle
from boomerang.data.network import networkDataHandle
from boomerang.data.validated import ValidatedDict

class BoomerangWebui():
    '''
    Routing for all webui stuff
    '''
    def setupRoutes(app:Flask):
        '''
        Given the webui app, register the pages.
        '''
        @app.route('/web/')
        def top():
            return render_template('web.html')

        @app.route('/web/allscores')
        def allscores():
            scores = scoreDataHandle.getAllScores()
            webscores = []
            for score in scores:
                data = {
                    'username': userDataHandle.userFromUserID(score.get('userid')).get_dict('data').get_str('name', "Newcomer"),
                    'title': songDataHandle.getSongFromId(score.get('songid')).get_str('title'),
                    'artist': songDataHandle.getSongFromId(score.get('songid')).get_str('artist'),
                    'chart': score.get('chart'),
                    'id': score.get('id')
                }
                webscores.append(data)

            return render_template('allscores.html', scores = webscores)

        @app.route('/icons/<path:filename>')
        def icons(filename):
            return send_from_directory('./boomerang/web/assets/profileicn', filename)

        @app.route('/web/makeuser', methods = ['GET','POST'])
        def adduser():
            if request.method == 'GET':
                return render_template('adduser.html', iconlist = networkDataHandle.getIconList())
        
            if request.method == 'POST':
                letters = string.ascii_letters

                cardid = request.form['cardid']
                if cardid == "":
                    cardid = 'C'+''.join(random.choice(letters) for i in range(19))
                    while userDataHandle.checkForCardid(cardid):
                        cardid = 'C'+''.join(random.choice(letters) for i in range(19))
                if userDataHandle.checkForCardid(cardid):
                    return "This card is already in use!"

                username = request.form['username']
                iconid = request.form['iconid']
                if username == "":
                    return "Username cannot be blank!"
                elif iconid == "Profile Icon":
                    return "Please select an Icon"

                userdata = ValidatedDict({
                    'name':username,
                    'iconid':int(iconid)
                })

                user = ValidatedDict(
                    {
                        'cardid': cardid,
                        'data': userdata
                    }
                )

                userDataHandle.createNewUser(user)

                return render_template('usercreated.html', username = username, cardid = cardid)