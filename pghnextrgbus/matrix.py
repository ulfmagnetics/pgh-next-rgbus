from __future__ import absolute_import
from __future__ import division
from builtins import object
from past.utils import old_div
from envparse import env
from itertools import chain
from datetime import timedelta
from rgbmatrix import RGBMatrix, graphics
import threading
import time
from . import utils

# TODO these should be exposed as config variables
URGENCY_COLORS = {'green': 15, 'yellow': 10, 'red': 5}

class Renderer(threading.Thread):
    def __init__(self, matrix, locators, delay=5):
        super(Renderer, self).__init__()
        self.matrix = matrix
        self.locators = locators
        self.delay = delay

    def arrivals_to_render(self):
        arrivals = chain(map(lambda locator: locator.next_arrivals(), self.locators))
        return sorted(arrivals, key=arrival.route)

    def run(self):
        while True:
            arrivals = self.arrivals_to_render()
            if len(arrivals) > 0:
                for arrival in arrivals:
                    self.matrix.clear()
                    self.matrix.render_arrival(arrival)
                    time.sleep(self.delay)
            else:
                self.matrix.clear()
                self.matrix.render_no_arrivals()
                time.sleep(self.delay)

class Matrix(object):
    def __init__(self, rows=16, chain_length=1, font_width='5', font_height='8'):
        self.rgbmatrix = RGBMatrix(rows, chain_length)
        self.font_width = int(font_width)
        self.font_height = int(font_height)
        self.font = graphics.Font()
        self.font.LoadFont("fonts/{0}x{1}.bdf".format(font_width, font_height))
        self.canvas = self.rgbmatrix.CreateFrameCanvas()

    def clear(self):
        utils.debug("Matrix cleared")
        self.canvas.Clear()

    def render_arrival(self, arrival):
        utils.debug(arrival)
        eta = arrival.eta()
        if eta < timedelta(minutes=1):
            minutes = 1
            eta_text = "<1 min!"
        else:
            minutes = old_div(eta.seconds, 60)
            eta_text = "{0} min".format(minutes)
        self.render_line(1, arrival.route, 0xff00ff)
        self.render_line(2, eta_text, self.urgency_color(minutes))
        self.canvas = self.rgbmatrix.SwapOnVSync(self.canvas)

    def render_no_arrivals(self):
        self.render_line(1, "No :(", 0xff00ff)
        self.render_line(2, "Buses", 0xff00ff)
        self.canvas = self.rgbmatrix.SwapOnVSync(self.canvas)

    def render_line(self, line_num, text, rgb):
        y_offset = (line_num - 0) * self.font_height - 1
        r = (rgb >> 16) & 0xff
        g = (rgb >>  8) & 0xff
        b = (rgb >>  0) & 0xff
        text_color = graphics.Color(r, g, b)
        graphics.DrawText(self.canvas, self.font, 1, y_offset, text_color, text)

    def urgency_color(self, minutes):
        global URGENCY_COLORS
        if minutes >= URGENCY_COLORS['green']:
            utils.debug("{0} minutes -- green".format(minutes))
            return 0x00ff00
        elif minutes >= URGENCY_COLORS['yellow'] and minutes < URGENCY_COLORS['green']:
            utils.debug("{0} minutes -- yellow".format(minutes))
            return 0xffff00
        else:
            utils.debug("{0} minutes -- red".format(minutes))
            return 0xff0000

