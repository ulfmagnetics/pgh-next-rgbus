from collections import OrderedDict

class BustimeAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def predictions(stpid=""):
        """ Returns some random predictions for debugging """
        return OrderedDict([
            (u'prd',
             OrderedDict([(u'tmstmp', u'20140815 15:06:35'),
                          (u'typ', u'A'),
                          (u'stpnm', u'East Liberty Station stop A'),
                          (u'stpid', stpid),
                          (u'vid', u'3241'),
                          (u'dstp', u'955'),
                          (u'rt', u'P1'),
                          (u'rtdir', u'OUTBOUND'),
                          (u'des', u'East Busway to Swissvale'),
                          (u'prdtm', u'20140815 15:06:55'),
                          (u'tablockid', u'P1  -370'),
                          (u'tatripid', u'51924'),
                          (u'zone', None)])
             )
        ])

