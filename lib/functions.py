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
import urllib2
import getpass
import os
import base64

from os.path import expanduser

# curl interface
def curl_get_json(url):
    
    linkdata = get_linkdata()
    
    request = urllib2.Request( linkdata['url'] + url )
    base64string = base64.encodestring('%s:%s' % (linkdata['user'], linkdata['passwd'])).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.get_method = lambda: 'GET'
    
    result = urllib2.urlopen(request)
    cnt = result.read()
    result.close()
    
    return json.loads(cnt)
    
    
# Credentials via manual input if not saved
def get_linkdata():
    linkdatafile = expanduser("~") + "/.gl2t_linkdata"
    
    if os.access(linkdatafile, os.R_OK):
        with open(linkdatafile) as data_file:    
            data = json.load(data_file)
            return data
    else:
        return read_link_data()

# Query linkdata on commandline 
def read_link_data():
    url = raw_input("Graylog connection url: ")
    user = raw_input("Username: ")
    passwd = getpass.getpass("Password (no visible output ): ")
    
    linkdata = { "url" : url, "user" : user, "passwd" : passwd }
    
    return linkdata

# JSON Formated prints
def print_json_oneline(data):
    print json.dumps(data)
    
def print_json_nosort(data):
    print json.dumps(data, indent=4)
    
def print_json_nice(data):
    print json.dumps(data, indent=4, sort_keys=True)