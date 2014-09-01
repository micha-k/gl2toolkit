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

import lib.functions as func
import json

usage = "./gl2toolkit.py link (status|jvm|fields|tdump)"

def show_status(arg):
    return status_for_url('/system');

def show_jvmstatus(arg):
    return status_for_url('/system/jvm');
    
def show_threaddump(arg):
    print func.curl_get_plain('/system/threaddump');
    return 0;
  
def show_fields(arg):
    return status_for_url('/system/fields');
    

# Meta method for simple status
def status_for_url(url):
    data = func.curl_get_json(url);
    func.print_json_nice(data);
    
    return 0;
    

# Available commands
commands = {
    "status" : show_status,
    "jvm" : show_jvmstatus,
    "fields" : show_fields,
    "tdump" : show_threaddump
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