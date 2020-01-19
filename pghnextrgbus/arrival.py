from builtins import object
import pytz
from datetime import datetime

class Arrival(object):
    """ Presents bus arrival info in a ready-to-display manner. """

    @classmethod
    def from_prediction(cls, prediction):
        return cls(prediction.route, prediction.generated, prediction.eta)

    def __init__(self, route, generated_at, arriving_at):
        self.route = route
        self.generated_at = generated_at
        self.arriving_at = arriving_at

    def age(self):
        """ Returns the timedelta representing the amount of time that has
            elapsed since this prediction was generated. """
        return self.current_time() - self.generated_at

    def eta(self):
        """ Returns the ETA of the arriving bus, based on the initial
            arrival time and taking into account the age of the prediction. """
        return self.arriving_at - self.generated_at - self.age()

    def current_time(self):
        return datetime.now(pytz.timezone('US/Eastern'))

    def __str__(self):
        return "Route {0}: ETA {1} (arriving at {2}, generated at {3}, age={4})".format(
            self.route, self.eta(), self.arriving_at, self.generated_at, self.age()
        )

    @property
    def route(self):
        return self.route

    @property
    def generated_at(self):
        return self.generated_at

    @property
    def arriving_at(self):
        return self.arriving_at
