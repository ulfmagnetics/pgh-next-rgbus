from pghbustime import Prediction, BustimeAPI
from arrival import Arrival

class Locator(object):
    valid_directions = ['inbound', 'outbound']

    __api = None

    def __init__(self, api_key="", stop_id="", direction=""):
        self.stop_id = stop_id
        if direction in self.__class__.valid_directions:
            self.direction = direction
        else:
            raise ValueError('Invalid direction -- must be in {0}'.format(self.__class__.valid_directions))

    def next_arrivals(self):
        arrivals = []
        for v in self.predictions():
            if v['rtdir'].lower() == self.direction:
                prediction = Prediction.fromapi(self.api(), v)
                arrival = Arrival.from_prediction(prediction)
                arrivals.append(arrival)
        return arrivals

    def api(self):
        if not self.__class__.__api:
            self.__class__.__api = BustimeAPI(api_key)
        return self.__class__.__api

    def predictions(self):
        response = self.api().predictions(stpid=self.stop_id)
        try:
            return response['prd']
        except KeyError:
            return {}
