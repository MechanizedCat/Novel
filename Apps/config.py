import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BasicCon:

    CSRF_ENABLED = True
    SECRET_KEY = 'YOU Guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CHAPTER_PER_PAGE = 20
    SSL_DISABLE = True

class DevCon(BasicCon):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    DEBUG = True


class ProCon(BasicCon):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
    'dev': DevCon,
    'default': DevCon,
    'product': ProCon
}