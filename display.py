#!/usr/bin/python

import os, sys
from os import getuid
from time import sleep

if (getuid() != 0):
  print "This script must be run as root!"
  sys.exit(1)

sys.path.append('lib')
from rgbmatrix import Adafruit_RGBmatrix

ROWS = 16
CHAIN_LENGTH = 1
matrix = Adafruit_RGBmatrix(ROWS, CHAIN_LENGTH)

# TODO display spinner while loading

font_width  = 4
font_height = 6
bdf_font_file = "fonts/{0}x{1}.bdf".format(font_width, font_height)

matrix.DrawText(bdf_font_file, 0, 0, 0xFF, 0, 0xFF, "TODO")
sleep(10.0)

matrix.Clear()

