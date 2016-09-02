class Arrival(object):
    """ Presents bus arrival info in a ready-to-display manner. """

    @classmethod
    def from_prediction(cls, prediction):
        return cls(prediction.route, prediction.eta - prediction.generated)

    def __init__(self, route, eta_seconds):
        self.route = route
        self.eta_seconds = eta_seconds

    def humanized_eta(self):
        # TODO '<1 minute', '2 minutes', etc...
        return "{0} seconds".format(self.eta_seconds)

    def to_s(self):
        "Route {0} arrives in {1}".format(self.route, self.humanized_eta())
