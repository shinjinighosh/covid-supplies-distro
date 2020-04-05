#!/usr/bin/env python3

import json

from flask import Flask, url_for, request, render_template, json
from argparse import ArgumentParser

import loginhelp

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '.'

@app.route('/login')
def login():
    return render_template('index.html', stuff=render_template('login.html'))


@app.route('/')
def index():
    return login()


@app.route('/login/check', methods=['POST'])
def login_check():
    reqdata = request.get_json()
    data = dict()
    for entry in reqdata:
        data[entry['name']] = entry['value']
    valid = loginhelp.check(data['user'], data['pwd'])
    if valid:
        role = data['role']

        response = app.response_class(status=200, response=json.dumps({'message': 'login success'}),
                                      mimetype='application/json')

    else:
        response = app.response_class(status=400, response=json.dumps({'message': 'invalid login credentials'}),
                                      mimetype='application/json')

    return response

if __name__ == "__main__":
    app.run()
