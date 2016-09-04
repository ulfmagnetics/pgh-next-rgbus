from envparse import env
from datetime import timedelta
from rgbmatrix import Adafruit_RGBmatrix

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
            eta_text = "<1 min!"
        else:
            minutes = eta.seconds / 60
            eta_text = "{0} min".format(minutes)
        self.render_line(1, arrival.route, 0xff, 0, 0xff)
        # TODO conditional colors based on ETA urgency!
        self.render_line(2, eta_text, 0xff, 0xff, 0)

    def render_line(self, line_num, text, r, g, b):
        y_offset = (line_num - 1) * self.font_height
        self.rgbmatrix.DrawText(self.bdf_font_file, 1, y_offset, r, g, b, text)

    def debug(self, msg):
        if env('DEBUG', default=False, cast=bool):
            print msg

