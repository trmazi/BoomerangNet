from flask import Flask, render_template
from flask_restful import Api
import argparse
import os

# Import the services
from boomerang.services.routes.routestatics import routeStatics
from boomerang.services.routes.machineroutes import machineRoutes
from boomerang.services.routes.ranking import routeRanking
from boomerang.services.routes.notice import routeNotices
from boomerang.services.routes.servdata import routeBaseData
from boomerang.services.routes.music import routeMusic
from boomerang.services.routes.auth import routeAuth
from boomerang.services.routes.users import routeUsers
from boomerang.services.routes.stages import routeStages

# Import the webui
from boomerang.utils.webui import BoomerangWebui

# Import DB stuff
import boomerang.data.sql

app = Flask(__name__, template_folder=os.path.abspath('./boomerang/web/templates'))
api = Api(app)

# Load the webui
BoomerangWebui.setupRoutes(app)

# Route the rest
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/services')
def services():
    return "If you're reading this, services are OK!"

# Start using the imports
api.add_resource(routeStatics.routeEmergency, '/services/Emergency.txt')
api.add_resource(routeStatics.routeNewSongEvent, '/services/newsongevent.txt')
api.add_resource(machineRoutes.routeMachinePoints, '/services/games/gameCenters/points/machine/<string:machine_id>')
api.add_resource(routeRanking.bootupRanking, '/services/games/bestRankings')
api.add_resource(routeNotices, '/services/games/notices')
api.add_resource(routeBaseData.routeUserLevelTable, '/services/baseData/userLevelTable')
api.add_resource(routeMusic.routeMusicBestRankings, '/services/music/<string:music_id>/user/<user_id>/bestRankings')
api.add_resource(routeMusic.routeGuestMusicBestRankings, '/services/music/<string:music_id>/user/bestRankings')
api.add_resource(routeMusic.routeNearRankings, '/services/music/<music_id>/nearRankings')
api.add_resource(routeAuth.noCardLogin, '/services/auth/noCardLogin')
api.add_resource(routeAuth.login, '/services/auth/login')
api.add_resource(routeUsers.routeUserGet, '/services/users/<string:user_id>')
api.add_resource(routeUsers.routeGuestUserConfig, '/services/users//configurations')
api.add_resource(routeUsers.routeUserConfig, '/services/users/<user_id>/configurations')
api.add_resource(routeStages.routeUserMusicHistories, '/services/stages/user/<user_id>/music/histories')
api.add_resource(routeStages.routeUserFinalHistories, '/services/stages/user/<user_id>/final/histories')
api.add_resource(routeStages.routeGuestUserMusicHistories, '/services/stages/user//music/histories')
api.add_resource(routeStages.routeGuestUserFinalHistories, '/services/stages/user//final/histories')
api.add_resource(routeStages.routeStageNearRankings, '/services/stages/nearRankings')

def main() -> None:
    parser = argparse.ArgumentParser(description="BoomerangNet: A 3rd party network for Beatcraft Cyclon, written in Flask.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    boomerang.data.sql.setupDatabase
    app.run(host='0.0.0.0', port=args.port, debug=False)

if __name__ == '__main__':
    main()