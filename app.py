import flask
from flask import request
from sklearn.externals import joblib
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import PolynomialFeatures


model=joblib.load("/content/ObesemodelPoly3.ml")
app=flask.Flask(__name__)
#from flask_core import CORS


CORS(app)

@app.route("/")

def default():
    poly=PolynomialFeatures(3)
    xx=poly.fit_transform([[21,1,1,1,80,3,1]])
    return model.predict(xx)

app.run()

'''
pip install --global-option=build_ext \
            --global-option="-I/usr/local/opt/openssl/include" \
            --global-option="-L/usr/local/opt/openssl/lib" psycopg2

'''