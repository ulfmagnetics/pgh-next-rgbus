from .context import pghnextrgbus
import pytest
from pytest_mock import mocker
from collections import OrderedDict

@pytest.fixture
def api_mocks(mocker):
    mocker.patch.object(pghnextrgbus.Prediction, 'fromapi')
    mocker.patch.object(pghnextrgbus.Arrival, 'from_prediction')

@pytest.fixture
def locator(mocker):
    stop_id = "7637"
    direction = "inbound"
    locator = pghnextrgbus.Locator(stop_id=stop_id, direction=direction)
    mocker.patch.object(locator, 'api')
    return locator

def prediction(stop_id="7637", route="P1", direction="inbound"):
    return OrderedDict({
        'tmstmp': '20140815 15:06:35',
        'typ': 'A',
        'stpnm': 'East Liberty Station stop A',
        'stpid': stop_id,
        'vid': '3241',
        'dstp': '955',
        'rt': route,
        'rtdir': direction.upper(),
        'des': 'East Busway to Swissvale',
        'prdtm': '20140815 15:06:55',
        'tablockid': 'P1  -370',
        'tatripid': '51924',
        'zone': None
    })

# with a single prediction, pgh-bustime returns a single OrderedDict
def test_next_arrivals_single_prediction(api_mocks, locator, mocker):
    mocker.patch.object(locator, 'predictions')
    locator.predictions.return_value = prediction(direction="inbound")
    arrivals = locator.next_arrivals()
    assert len(arrivals) == 1

# with multiple predictions, pgh-bustime returns a list of OrderedDicts
def test_next_arrivals_multiple_predictions(api_mocks, locator, mocker):
    mocker.patch.object(locator, 'predictions')
    locator.predictions.return_value = [
        prediction(route="T1",direction="inbound"),
        prediction(route="T2",direction="inbound"),
        prediction(direction="outbound")
    ]
    arrivals = locator.next_arrivals()
    assert len(arrivals) == 2

