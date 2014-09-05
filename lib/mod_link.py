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

from os.path import expanduser

import os
import json
import lib.functions as func

linkdatafile = expanduser("~") + "/.gl2t_linkdata"

usage = "./gl2toolkit.py link (set|unset|show)"

# Set access url and userdata (optinal)
def set_linkdata(arg):
    linkdata = func.read_link_data()
    with open(linkdatafile, 'w') as outfile:
      json.dump(linkdata, outfile)
    
    os.chmod(linkdatafile, 0600)
    
    return 0
    
# unset linkdata
def unset_linkdata(arg):
    if os.access(linkdatafile, os.W_OK):
        os.remove(linkdatafile)
        return 0
    else:
        return 1
    
# display linkdata
def show_linkdata(arg):

    if os.access(linkdatafile, os.R_OK):
        with open(linkdatafile) as data_file:    
            data = json.load(data_file)
    
            if len(data["passwd"]) > 0:
                data["passwd"] = "*************"
    
                func.print_json_nosort(data)
    
    else:
        print "{ }"
        
    return 0

# Available commands
commands = {
    "set" : set_linkdata,
    "unset" : unset_linkdata,
    "show" :  show_linkdata
}

# Evaluate request
def eval(arg):
    if len(arg) > 2:
        cmd = arg[2]
        try:
            return commands[cmd](arg)
        except KeyError:
            print usage
            return 1
    else:
        print usage
        return 0