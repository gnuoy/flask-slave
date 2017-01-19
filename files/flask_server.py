#!/usr/bin/python3

from flask import Flask
import os
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.config.from_pyfile('/opt/flask_slave/conf/flask_config.cfg')
    app.run(host='0.0.0.0')
