import sqlite3
import datetime
import string
import random
import time
import requests
import numpy as np


def request_handler(request):
    # Request Dictionary: {'method': 'GET', 'args': ['yo', 'hey'], 'values': {'yo': '11', 'hey': '5'}}
    if request['method'] != 'GET': #POST request
        if 'user' not in request['form'].keys():
            return "You must enter a use, current keys are", request['form'].keys()
        # POST request
        try:
            user = request['form']['user']
        except:
            return "User should be string"
        outs = POST(user)
        return str(outs)
    # GET request
    else:
        result = GET()
        return result



supplies_db = "supplies.db"

def GET():
    conn = sqlite3.connect(supplies_db)  # connect to that database (will create if it doesn't already exist)
    c = conn.cursor()  # move cursor into database (allows us to execute commands)
    c.execute('''CREATE TABLE IF NOT EXISTS supplies (user text, timing timestamp);''') # run a CREATE TABLE command
    thirty_seconds_ago = datetime.datetime.now()- datetime.timedelta(seconds = 30)
    things = c.execute('''SELECT user FROM supplies WHERE timing > ? ORDER BY timing DESC;''',(thirty_seconds_ago,)).fetchall()
    outs = []
    for x in things:
        outs.append(x)
    conn.commit() # commit commands
    conn.close() # close connection to database
    return outs

def POST(user):
    conn = sqlite3.connect(shards_db)  # connect to that database (will create if it doesn't already exist)
    c = conn.cursor()  # move cursor into database (allows us to execute commands)
    c.execute('''CREATE TABLE IF NOT EXISTS supplies (user text, timing timestamp);''') # run a CREATE TABLE command
    c.execute('''INSERT into supplies VALUES (?,?,?,?);''',(user,datetime.datetime.now())) #with time
    conn.commit() # commit commands
    conn.close() # close connection to database
    return "Successfully entered value"


# request = {'method': 'POST', 'form': {'user': 'Shinjini'}}
# print(request_handler(request))
# request = {'method': 'GET', 'args': ['values'], 'values': {}}
# request = {'method': 'GET', 'args': []}
# print(request_handler(request))
