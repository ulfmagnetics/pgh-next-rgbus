from envparse import env
from locator import Locator
import time

def main(args):
    poll_interval = env('POLL_INTERVAL', default=30, cast=int)
    api_key       = env('API_KEY')
    stop_id       = env('STOP_ID')
    direction     = env('DIRECTION')

    locator = Locator(api_key=api_key, stop_id=stop_id, direction=direction)
    while True:
        for arrival in locator.next_arrivals():
            print arrival

        time.sleep(poll_interval)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
