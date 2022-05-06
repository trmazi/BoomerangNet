import os

class StaticPath:
    def getStaticPath():
        return os.path.abspath(os.path.dirname(__file__))