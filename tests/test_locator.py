from .context import pghnextrgbus
from pytest_mock import mocker
from collections import OrderedDict

def prediction(stop_id="7637", route="P1", direction="inbound"):
    return {
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
    }

def test_next_arrivals(mocker):
    stop_id = "7637"
    direction = "inbound"
    locator = pghnextrgbus.Locator(stop_id=stop_id, direction=direction)

    mocker.patch.object(locator, 'api')
    mocker.patch.object(pghnextrgbus.Prediction, 'fromapi')
    mocker.patch.object(pghnextrgbus.Arrival, 'from_prediction')

    mocker.patch.object(locator, 'predictions')
    locator.predictions.return_value = [
        prediction(route="T1",direction="inbound"),
        prediction(route="T2",direction="inbound"),
        prediction(direction="outbound")
    ]
    arrivals = locator.next_arrivals()
    assert len(arrivals) == 2

