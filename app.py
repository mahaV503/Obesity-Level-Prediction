import flask
from flask import request

app=flask.Flask(__name__)

from flask_core import CORS

CORS(app)

@app.route("/")

def default():
    return "<h1> API SERVER IS working<h1>"
    