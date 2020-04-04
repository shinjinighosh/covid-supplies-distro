#!/usr/bin/env python3

import json

from flask import Flask, url_for, request, render_template, json
from argparse import ArgumentParser

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
    data = request.get_json()
    print(data)

    response = app.response_class(status=200, response=json.dumps({}),
                                  mimetype='application/json')

    return response

if __name__ == "__main__":
    app.run()
