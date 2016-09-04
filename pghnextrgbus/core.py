from envparse import env
from locator import Locator
from matrix import Matrix
import time
import signal
import sys

matrix = None

def sigint_handler(signal, frame):
    global matrix
    if matrix:
        matrix.clear()
    sys.exit(0)

def main(args):
    poll_interval = env('POLL_INTERVAL', default=30, cast=int)
    api_key       = env('API_KEY')
    stop_id       = env('STOP_ID')
    direction     = env('DIRECTION')
    matrix_rows   = env('MATRIX_ROWS', default=16, cast=int)
    matrix_chain_length = env('MATRIX_CHAIN_LENGTH', default=1, cast=int)

    global matrix
    matrix = Matrix(rows=matrix_rows, chain_length=matrix_chain_length)
    locator = Locator(api_key=api_key, stop_id=stop_id, direction=direction)

    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        # FIXME need to loop over all arrivals until poll interval expires
        for arrival in locator.next_arrivals():
            matrix.clear()
            matrix.render_arrival(arrival)
            time.sleep(5)
        time.sleep(poll_interval)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
