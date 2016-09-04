import os
if 'MOCKAPI' in os.environ and os.environ['MOCKAPI']:
    print "--- MOCK API ---"
    from mockapi import BustimeAPI
else:
    from pghbustime import BustimeAPI
from pghbustime import Prediction
from arrival import Arrival
from collections import OrderedDict

class Locator(object):
    valid_directions = ['inbound', 'outbound']

    __api = None

    def __init__(self, api_key="", stop_id="", direction=""):
        self.api_key = api_key
        self.stop_id = stop_id
        if direction in self.__class__.valid_directions:
            self.direction = direction
        else:
            raise ValueError('Invalid direction -- must be in {0}'.format(self.__class__.valid_directions))

    def next_arrivals(self):
        """ Returns a list of Arrivals for each upcoming predicted
            arrival at self.stop_id """
        arrivals = []
        prd = self.predictions()
        if type(prd) == OrderedDict:
            arrival = self.__arrival_from_raw_prediction(prd)
            arrivals.append(arrival)
        else:
            for p in prd:
                if p['rtdir'].lower() == self.direction:
                    arrival = self.__arrival_from_raw_prediction(p)
                    arrivals.append(arrival)
        return arrivals

    def api(self):
        if not self.__class__.__api:
            self.__class__.__api = BustimeAPI(self.api_key)
        return self.__class__.__api

    def predictions(self):
        response = self.api().predictions(stpid=self.stop_id)
        try:
            print response['prd']
            return response['prd']
        except KeyError:
            return {}

    def __arrival_from_raw_prediction(self, prd):
        prediction = Prediction.fromapi(self.api(), prd)
        arrival = Arrival.from_prediction(prediction)

