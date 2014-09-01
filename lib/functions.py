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

import json


# JSON Formated prints
def print_json_oneline(data):
    print json.dumps(data)
    
def print_json_nosort(data):
    print json.dumps(data, indent=4)
    
def print_json_nice(data):
    print json.dumps(data, indent=4, sort_keys=True)