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
import getpass
import os
import base64
import httplib
import urllib

from os.path import expanduser

# curl data types
def curl_get_json(url):
    return json.loads(curl_get(url)["data"])

def curl_get_plain(url):
    return curl_get(url)["data"]


# Curl methods
def curl_get(url):
    linkdata = get_linkdata()
    base64string = base64.encodestring('%s:%s' % (linkdata['user'], linkdata['passwd'])).replace('\n', '')    
    
    conn = httplib.HTTPConnection( linkdata['host'], int(linkdata['port']) )
    conn.putrequest("GET", url)
    conn.putheader("Authorization", "Basic %s" % base64string)
    conn.putheader("User-Agent", "gl2toolkit/1")
    conn.endheaders()
    conn.send("")
    
    response = conn.getresponse()
    res_dict = { "status" : response.status , "reason" : response.reason , "data" : response.read() }
    
    return res_dict
    
def curl_put(url, body):
    linkdata = get_linkdata()
    bodyString = json.dumps(body)
    base64string = base64.encodestring('%s:%s' % (linkdata['user'], linkdata['passwd'])).replace('\n', '')    
    
    conn = httplib.HTTPConnection( linkdata['host'], int(linkdata['port']) )
        
    conn.putrequest("PUT", url)
    conn.putheader("Authorization", "Basic %s" % base64string)
    conn.putheader("Content-Type", 'application/json; charset=utf-8')
    conn.putheader("Accept", "application/json")
    conn.putheader("Accept-Charset", "utf-8")
    conn.putheader("User-Agent", "gl2toolkit/1")
    conn.putheader("Content-Length",len(bodyString))
    conn.endheaders( bodyString )
    conn.send("")
    
    response = conn.getresponse()
    res_dict = { "status" : response.status , "reason" : response.reason}
    
    return res_dict
    
    
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
    host = raw_input("Graylog host: ")
    port = raw_input("Graylog api port: ")
    user = raw_input("Username: ")
    passwd = getpass.getpass("Password (no visible output ): ")
    
    linkdata = { "host" : host, "port" : port, "user" : user, "passwd" : passwd }
    
    return linkdata

# JSON Formated prints
def print_json_oneline(data):
    print json.dumps(data)
    
def print_json_nosort(data):
    print json.dumps(data, indent=4)
    
def print_json_nice(data):
    print json.dumps(data, indent=4, sort_keys=True)
    