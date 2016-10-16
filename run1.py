# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<H1> this is a test! </H1>"
if __name__ == '__main__':
    app.run()
