# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, HEROKU'

if __name__ == '__main__':
    app.run()