## -*- coding: utf-8 -*-
##
##  Jonathan Salwan - 2014-05-17 - ROPgadget tool
##
##  http://twitter.com/JonathanSalwan
##  http://shell-storm.org/project/ROPgadget/
##

import re
import codecs
import ropgadget.roplib.rgutils as rgutils
import sqlite3

from ropgadget.roplib.binary             import Binary
from capstone                            import CS_MODE_32
from ropgadget.roplib.gadgets            import Gadgets
from ropgadget.roplib.options            import Options
from ropgadget.roplib.ropchain.ropmaker  import ROPMaker
from ropgadget.roplib.core            import Core

class Main(object):
    def __init__(self, options):
        self.__options = options
        self.__binary  = None
        self.__gadgets = []
        self.__offset  = 0
        self.prompt    = '(ROPgadget)> '

    def runCore(self):
        Core(self.__options).analyze()
