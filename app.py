import flask
from flask import request

app=flask.Flask(__name__)
from flask_cors import CORS, cross_origin
#from flask_core import CORS

CORS(app)

@app.route("/")

def default():
    return "<h1> API SERVER IS working<h1>"

app.run()

'''
pip install --global-option=build_ext \
            --global-option="-I/usr/local/opt/openssl/include" \
            --global-option="-L/usr/local/opt/openssl/lib" psycopg2

'''