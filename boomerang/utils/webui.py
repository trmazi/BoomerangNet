from flask import Flask, render_template, request, url_for, send_from_directory, redirect
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
                    return render_template('status.html', func = "Create User", status = "FAILURE!", status2 = "Username cannot be blank.", redir = url_for('adduser'))
                elif iconid == "Profile Icon":
                    return render_template('status.html', func = "Create User", status = "FAILURE!", status2 = "Please set an icon.", redir = url_for('adduser'))

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

        @app.route('/web/loaduser', methods = ['GET','POST'])
        def loaduser():
            if request.method == 'GET':
                return render_template('loaduser.html')

            if request.method == 'POST':
                cardid = request.form['cardid']
                if not userDataHandle.checkForCardid(cardid):
                    return render_template('status.html', func = "Update User", status = "FAILURE!", status2 = "The card you suppled doesn't exist.", redir = url_for('loaduser'))
                
                user, status = userDataHandle.userFromCardID(cardid)
                if not status:
                    return render_template('status.html', func = "Update User", status = "FAILURE!", status2 = "There was an issue loading your profile.", redir = url_for('loaduser'))

                userdata = user.get_dict('data')

                userid = user.get_int('id', None)
                username = userdata.get_str('name', "Newcomer")
                iconid = userdata.get_int('iconid', 1)

                return redirect(url_for('edituser') + f"?username={username}&iconid={iconid}&id={userid}")

        @app.route('/web/edituser', methods = ['GET', 'POST'])
        def edituser():
            if request.method == 'GET':
                username = request.args.get('username')
                iconid = request.args.get('iconid')
                id = request.args.get('id')
                if username == None:
                    return "No username was sent."
                elif iconid == None:
                    return "No iconid was sent."
                elif id == None:
                    return "No id was sent."

                return render_template('edituser.html', username=username, iconid=iconid, iconlist = networkDataHandle.getIconList(), userid = id)

            if request.method == 'POST':
                username = request.form['username']
                iconid = request.form['iconid']
                userid = request.form['userid']
                if username == "":
                    return render_template('status.html', func = "Update User", status = "FAILURE!", status2 = "Username cannot be blank.", redir = "")
                elif iconid == "Profile Icon":
                    return render_template('status.html', func = "Update User", status = "FAILURE!", status2 = "Please set an icon.", redir = "")

                user = userDataHandle.userFromUserID(int(userid))
                userdata = user.get_dict('data')

                userdata.replace_int('iconid', int(iconid))
                userdata.replace_str('name', username)

                user.replace_dict('data', userdata)

                userDataHandle.putUserFromUserID(int(userid), user)

                return render_template('status.html', func = "Update User", status = "Success!", status2 = "You will be redirected to the userlist in 5 secs.", redir = url_for('top'))