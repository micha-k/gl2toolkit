#!/usr/bin/env python
# 
# Copyright (c) 2014 Michael Kessel
# 
# This file is part of gl2toolkit
#
# This program is free software under the terms of the MIT License 
# You should have received a copy of the MIT License
# along with this program; if not, see <http://opensource.org/licenses/MIT>.
#

import sys

import lib.functions
import lib.mod_link
import lib.mod_system
import lib.mod_user

modules = {
    "link" : lib.mod_link,
    "system" : lib.mod_system,
    "user" : lib.mod_user
}

def print_modules():
    print "Valid major commands are:"
    for module in modules:
        print module

def main(arg):
    
    if len(arg) == 1:
        print_modules();
        rc = 0
    else: 
        (self, modul) = arg[:2]
        try:
            rc = modules[modul].eval(arg)
        except KeyError:
            print "Invalid major command:", modul
            rc = 1
            print
            print_modules()
    
    sys.exit(rc)

if __name__ == '__main__':
    main(sys.argv)