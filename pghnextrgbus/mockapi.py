from collections import OrderedDict
import datetime
import random

class BustimeAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def __prediction(self, eta_seconds=None, rt="P1", rtdir="INBOUND", stpid=""):
        if not eta_seconds:
            eta_seconds = random.randint(30, 900)
        generated_at = datetime.datetime.today()
        arriving_at  = generated_at + datetime.timedelta(seconds=eta_seconds)
        return OrderedDict([
            (u'tmstmp', generated_at.strftime('%Y%m%d %H:%M:%S')),
            (u'typ', u'A'),
            (u'stpnm', u'East Liberty Station stop A'),
            (u'stpid', stpid),
            (u'vid', u'3241'),
            (u'dstp', u'955'),
            (u'rt', rt),
            (u'rtdir', rtdir),
            (u'des', u'East Busway to Swissvale'),
            (u'prdtm', arriving_at.strftime('%Y%m%d %H:%M:%S')),
            (u'tablockid', u'P1  -370'),
            (u'tatripid', u'51924'),
            (u'zone', None)
        ])


    def predictions(self, num=3, stpid=""):
        """ Returns some random predictions for debugging """
        if num == 1:
            return OrderedDict({'prd': self.__prediction(stpid=stpid)})
        else:
            prd = []
            for _ in range(num):
                prd.append(self.__prediction(stpid=stpid))
            return OrderedDict({'prd': prd})

