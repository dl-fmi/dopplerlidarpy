#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dopplerlidarpy.utilities import arg_parser_tools as ap
from dopplerlidarpy.utilities.plot_dl import plot_dl

args = ap.my_args_parser()

plot_dl(args)
