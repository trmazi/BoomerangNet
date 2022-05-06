import os

class TemplatePath:
    def getTemplatePath():
        return os.path.abspath(os.path.dirname(__file__))