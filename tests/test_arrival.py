from .context import pghnextrgbus
from mock import Mock
from pytest_mock import mocker
import datetime

def now():
    return datetime.datetime(year=2016, month=9, day=2, hour=8, minute=30, second=0)

def route():
    return 'P1'

def an_arrival():
    eta = datetime.timedelta(minutes=5)
    return pghnextrgbus.Arrival(route(), now(), now() + eta)


def test_from_prediction():
    original_delta = datetime.timedelta(seconds=60)
    age_delta = datetime.timedelta(seconds=30)
    prediction = Mock(route=route(), eta=now() + original_delta, generated=now())
    arrival = pghnextrgbus.Arrival.from_prediction(prediction)
    assert type(arrival) is pghnextrgbus.Arrival
    assert arrival.route == route()
    assert arrival.generated_at == now()
    assert arrival.arriving_at == now() + original_delta

def test_age(mocker):
    arrival = an_arrival()
    mocked_now = mocker.patch.object(arrival, 'current_time')
    age_delta = datetime.timedelta(minutes=2)
    mocked_now.return_value = now() + age_delta
    assert arrival.age() == age_delta

def test_eta(mocker):
    arrival = an_arrival()
    mocker.patch.object(arrival, 'age')
    arrival.age.return_value = datetime.timedelta(minutes=2, seconds=00)
    assert arrival.eta() == datetime.timedelta(minutes=3, seconds=00)

