from envparse import env
from locator import Locator
from matrix import Renderer, Matrix
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

def main(args):
    global matrix, renderer
    poll_interval = env('POLL_INTERVAL', default=30, cast=int)
    display_delay = env('DISPLAY_DELAY', default=8, cast=int)
    api_key       = env('API_KEY')
    stop_id       = env('STOP_ID')
    direction     = env('DIRECTION')
    matrix_rows   = env('MATRIX_ROWS', default=16, cast=int)
    matrix_chain_length = env('MATRIX_CHAIN_LENGTH', default=1, cast=int)

    matrix = Matrix(rows=matrix_rows, chain_length=matrix_chain_length)
    locator = Locator(api_key=api_key, stop_id=stop_id, direction=direction)
    signal.signal(signal.SIGINT, sigint_handler)

    renderer = Renderer(matrix, delay=display_delay)
    renderer.daemon = True
    while True:
        renderer.arrivals = locator.next_arrivals()
        if not renderer.is_alive():
            renderer.start()
        time.sleep(poll_interval)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
