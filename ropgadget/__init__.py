## -*- coding: utf-8 -*-
##
##  Jonathan Salwan - 2014-05-12 - ROPgadget tool
##
##  http://twitter.com/JonathanSalwan
##  http://shell-storm.org/project/ROPgadget/
##

import ropgadget.args
import ropgadget.main
import ropgadget.roplib.options
import ropgadget.updateAlert
import ropgadget.version

def main():
    import sys
    from   ropgadget.args import Args
    from   ropgadget.main import Main
    sys.exit(Main(Args().getArgs()).runCore())
