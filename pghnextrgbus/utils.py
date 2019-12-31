# This module contains utility methods that can be shared across the app
from envparse import env
from datetime import datetime

def debug(msg):
    if env('DEBUG', default=False, cast=bool):
        print("[%s] %s" % (datetime.now().strftime("%c"), msg))
