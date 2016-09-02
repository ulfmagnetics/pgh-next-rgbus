import os
if os.environ['DEBUG']:
    from mockapi import BustimeAPI
else:
    from pghbustime import BustimeAPI
from arrival import Arrival

class Locator(object):
    valid_directions = ['inbound', 'outbound']

    def __init__(self, api_key="", stop_id="", direction=""):
        self.api = BustimeAPI(api_key)
        self.stop_id = stop_number
        if direction in self.__class__.valid_directions:
            self.direction = direction
        else:
            raise ValueError('Invalid direction -- must be in {0}'.format(self.__class__.valid_directions))

    def next_arrivals(self):
        predictions = api.predictions(stpid=stop_id)
        arrivals = []
        for k, v in predictions.items():
            if v['rtdir'].lower() == self.direction:
                arrival = Arrival.from_prediction(v)
                arrivals.append(arrival)
        return arrivals

