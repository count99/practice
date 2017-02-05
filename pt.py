# -*- coding: utf-8 -*-
# Created by Eli on 2017/2/17

import sys
import os

class Tools(object):

    def conda_update():
        os.system("conda update --all")
    def list_help():
        print("""
        -h: Help;
        -a: activate py3
        -d: deactivate
        -u: conda update
        """)

if __name__ == '__main__':

    funtions = sys.argv[-1]

    if funtions == "-u":
        Tools.conda_update()
    else:
        Tools.list_help()