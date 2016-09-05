from envparse import env
from datetime import timedelta
from rgbmatrix import Adafruit_RGBmatrix
import threading
import time

# TODO these should be exposed as config variables
URGENCY_COLORS = {'green': 15, 'yellow': 10, 'red': 5}

class Renderer(threading.Thread):
    def __init__(self, matrix, delay=5):
        super(Renderer, self).__init__()
        self.matrix = matrix
        self.delay = delay
        self._arrivals = []

    @property
    def arrivals(self): return self._arrivals

    @arrivals.setter
    def arrivals(self, value): self._arrivals = value

    def run(self):
        while True:
            for arrival in self._arrivals:
                self.matrix.clear()
                self.matrix.render_arrival(arrival)
                time.sleep(self.delay)

class Matrix(object):
    def __init__(self, rows=16, chain_length=1, font_width='5', font_height='8'):
        self.rgbmatrix = Adafruit_RGBmatrix(rows, chain_length)
        self.font_width = int(font_width)
        self.font_height = int(font_height)
        self.bdf_font_file = "fonts/{0}x{1}.bdf".format(font_width, font_height)

    def clear(self):
        self.debug("Matrix cleared")
        self.rgbmatrix.Clear()

    def render_arrival(self, arrival):
        self.debug(arrival)
        eta = arrival.eta()
        if eta < timedelta(minutes=1):
            minutes = 1
            eta_text = "<1 min!"
        else:
            minutes = eta.seconds / 60
            eta_text = "{0} min".format(minutes)
        self.render_line(1, arrival.route, 0xff00ff)
        self.render_line(2, eta_text, self.urgency_color(minutes))

    def render_line(self, line_num, text, rgb):
        y_offset = (line_num - 1) * self.font_height
        r = (rgb >> 16) & 0xff
        g = (rgb >>  8) & 0xff
        b = (rgb >>  0) & 0xff
        self.rgbmatrix.DrawText(self.bdf_font_file, 1, y_offset, r, g, b, text)

    def urgency_color(self, minutes):
        global URGENCY_COLORS
        if minutes >= URGENCY_COLORS['green']:
            return 0x00ff00
        elif minutes >= URGENCY_COLORS['yellow']:
            return 0xffff00
        else:
            return 0xff0000

    def debug(self, msg):
        if env('DEBUG', default=False, cast=bool):
            print msg

