from flask import Flask
from flask_restful import Api, Resource
import argparse

app = Flask(__name__)
api = Api(app)


def main() -> None:
    parser = argparse.ArgumentParser(description="BoomerangNet: A 3rd party network for Beatcraft Cyclon, written in Flask.")
    parser.add_argument("-p", "--port", help="Port to listen on. Defaults to 80", type=int, default=80)
    args = parser.parse_args()

    # Run the app
    app.run(host='0.0.0.0', port=args.port, debug=True)

if __name__ == '__main__':
    main()