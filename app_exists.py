#!/usr/bin/env python

import os.path
import sys
# path args are found in the script within filewave
path = sys.argv[1]

def App_query(path):
    if os.path.exists(path):
        print(path + 'is already installed')
        sys.exit(1)
    else:
        print(path + 'not installed, continue installation')
        sys.exit(0)

App_query(path)
