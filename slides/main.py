#!/usr/bin/env python3

import shutil
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

SLIDES_LOCATION = "/home/bird/.hackerslides/europython-2015-bokeh.md"


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/slides.md', methods=['GET'])
def get_slides():
    with open(SLIDES_LOCATION, encoding='utf-8') as fp:
        return fp.read()


@app.route('/slides.md', methods=['PUT'])
def save_slides():
    new_slides = request.get_data().decode('utf-8')
    with open(SLIDES_LOCATION, 'w', encoding='utf-8') as fp:
        fp.write(new_slides)
    return make_response("", 200)

if __name__ == '__main__':
    if not os.path.isfile(SLIDES_LOCATION):
        shutil.copy("initial-slides.md", SLIDES_LOCATION)
    app.run('0.0.0.0', 8000, debug=True)
