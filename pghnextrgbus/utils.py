# This module contains utility methods that can be shared across the app
from envparse import env

def debug(msg):
    if env('DEBUG', default=False, cast=bool):
        print msg
