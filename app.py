from flask import Flask
from flask import render_template
from flask import redirect
import json

app = Flask(__name__)

@app.route('/')
def indexpage():
    return "hello world"

@app.route('/photos')
def photos():
    with open('photos.json', 'r') as jsonFile:
        photoList = json.load(jsonFile)
    return render_template('photos.html', photosList = photoList)