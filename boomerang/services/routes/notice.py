from flask_restful import Resource

class routeNotices():
    '''
    Class for handling newsposts. For now,
    since we don't have a DB, this is bogus.
    '''
    def get(self):
        news = [{
            'noticeNo': 1000,
            'nation': 'KR',
            'title': 'Welcome to BoomerangNet!',
            'noticeType': 'event',
            'contentType': 'text',
            'content': 'A 3rd party network for Beatcraft Cyclon, written in Flask.',
            'content2': "We are glad to see you!",
            'image': '',
        }]

        data = {
            'notices': news
        }

        return data, 200