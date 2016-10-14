# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, redirect, url_for, flash,request

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1> this is a test! </h1>"
if __name__ == '__main__':
    app.run()
