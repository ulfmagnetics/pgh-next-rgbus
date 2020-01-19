from __future__ import absolute_import
from envparse import env
from .locator import Locator
from .matrix import Renderer, Matrix
import time
import signal
import sys

matrix = None
renderer = None

def sigint_handler(signal, frame):
    global matrix, renderer
    if matrix:
        matrix.clear()
    if renderer:
        renderer.join(1.0)
    sys.exit(0)

def parse_stop_ids(stop_ids):
    return [id_and_dir.split('/') for id_and_dir in stop_ids.split(',')]

def main(args):
    global matrix, renderer
    poll_interval = env('POLL_INTERVAL', default=30, cast=int)
    display_delay = env('DISPLAY_DELAY', default=8, cast=int)
    api_key       = env('API_KEY')
    stop_ids      = env('STOP_IDS') # using format: 7637/inbound,8475/outbound
    matrix_rows   = env('MATRIX_ROWS', default=16, cast=int)
    matrix_chain_length = env('MATRIX_CHAIN_LENGTH', default=1, cast=int)

    matrix = Matrix(rows=matrix_rows, chain_length=matrix_chain_length)
    locators = [Locator(api_key=api_key, stop_id=sid, direction=dir) for (sid,dir) in parse_stop_ids(stop_ids)]

    signal.signal(signal.SIGINT, sigint_handler)

    renderer = Renderer(matrix, locators, delay=display_delay)
    renderer.daemon = True
    while True:
        if not renderer.is_alive():
            renderer.start()
        time.sleep(poll_interval)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
