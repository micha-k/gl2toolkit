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

usage = "./gl2toolkit.py user list|fulldump|permdump|copyperm"

def list_users(arg):
    users = func.curl_get_json('/users');
    
    print "%25s %25s %25s %25s %6s" % ("Id:", "Username:", "Full name:", "E-Mail:", "Ldap?")
    
    for user in users['users']:
        print "%25s %25s %25s %25s %6s" % (user['id'], user['username'], user['full_name'], user['email'], user['external'])
    #func.print_json_nice(users)
    return 0
    
def show_fulldump(arg):
    usage = "./gl2toolkit.py user fulldump <username>|<id>"
    
    if len(arg) > 3:
        param = arg[3]
        user = get_user(param)
        func.print_json_nice(user)
        
        return 0
    else:
        return 1

def show_permdump(arg):
    usage = "./gl2toolkit.py user permdump <username>|<id> (streamonly|dashonly|streamdash)"
    
    if len(arg) > 3:
        param = arg[3]
        user = get_user(param)
        
        if len(arg) > 4:
            show_only = arg[4].lower()
            filtered_perm = filter_permissions(user, show_only)
            func.print_json_nice(filtered_perm)
        else:
            func.print_json_nice(user['permissions'])
        
        return 0
    else:
        return 1

def copy_perm(arg):
    usage = "./gl2toolkit.py user copyperm <username src> <username dst> (streamonly|dashonly)"
    
    if len(arg) > 4:
        selector = "streamdash"
        user_src = get_user(arg[3])
        user_dst = arg[4]
        
        if len(arg) > 5:
            selector = arg[5]
        
        if selector != "streamonly" and selector != "dashonly":
            selector = "streamdash"    
            
        filtered_perm = { "permissions" : filter_permissions(user_src, selector) }
        
        print "User src: " + user_src['username']
        print "User dest: " + user_dst
        func.print_json_nice(filtered_perm)
        
        res = func.curl_put('/users/'+ user_dst.strip() +'/permissions', filtered_perm )
        func.print_json_oneline(res)
        
        if res['status'] == 400:
            return 1
        else:
            return 0
    else:
        return 1

# Internal functions
def get_user(param):
    users = func.curl_get_json('/users');
    for user in users['users']:
        if user['username'] == param or user['id'] == param:
            return user

def filter_permissions(userData, filter):
    fperm = []
    
    if filter == "streamonly" or filter == "dashonly" or filter == "streamdash":
        for perm in userData['permissions']:
            if (filter == "streamonly" or filter == "streamdash") and perm.startswith('streams:'):
                fperm.append(perm)
            if (filter == "dashonly" or filter == "streamdash") and perm.startswith('dashboards:'):
                fperm.append(perm)        
    else:
        fperm = userData['permissions']
    
    return fperm

# Available commands
commands = {
    "list" : list_users,
    "fulldump" :  show_fulldump,
    "permdump" :  show_permdump,
    "copyperm" :  copy_perm
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