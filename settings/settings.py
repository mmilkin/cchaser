import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../chaser.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '../migrations')

# administrator list
ADMINS = ['redawn']

# Raspberry Pi address
PI_ADDRESS = '192.168.1.1'
IMG_PORT = '8080'

CSRF_ENABLED = True
SECRET_KEY = "5Jis&j1:&,:tFZg7[<M+N+9EAdr:wP]!^uo[N.i,)24Jw5R;kw|4;:YanBXlaJ(d')"

PORT = 7777
HOST = '0.0.0.0'

DEBUG = True

try:
    io = __import__('RPi.GPIO')
except ImportError:
    print 'could not import RPi.GPIO using stubIO'
    from chaser.stub_io import GPIO as io
