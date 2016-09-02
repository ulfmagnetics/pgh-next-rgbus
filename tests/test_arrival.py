from .context import pghnextrgbus
from mock import Mock
import datetime

def test_from_prediction():
    eta = datetime.datetime.now()
    generated = eta - datetime.timedelta(seconds=20)
    prediction = Mock(route='P1', eta=eta, generated=generated)
    arrival = pghnextrgbus.Arrival.from_prediction(prediction)
    assert arrival.route == 'P1'
    assert arrival.eta_seconds == 20
