import flask
from flask import request
#from sklearn.externals import joblib
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import PolynomialFeatures

import joblib

model=joblib.load("/Users/mvr/Documents/Mlproject/ObesemodelPoly3.ml")
app=flask.Flask(__name__)
#from flask_core import CORS

weight_dic={0:'Insufficient_Weight', 
            1:'Normal_Weight', 
            2:'Obesity_Type_I', 
            3:'Obesity_Type_II',
            4:'Obesity_Type_III', 
            5:'Overweight_Level_I', 
            6:'Overweight_Level_II'}


'''
top_features=norm_X[["Age","CAEC","family_history_with_overweight",
"CALC","Weight","CH2O","FAF"]]
'''

CORS(app)

@app.route("/")
def default():
    poly=PolynomialFeatures(3)
    xx=poly.fit_transform([[request.args['age'],
                            request.args['CAEC'],
                            request.args['family_history_with_overweight'],
                            request.args['CALC'],request.args['Weight'],
                            request.args['CH2O'],request.args['FAF']]])
    return weight_dic[model.predict(xx)[0]]

app.run()

'''
pip install --global-option=build_ext \
            --global-option="-I/usr/local/opt/openssl/include" \
            --global-option="-L/usr/local/opt/openssl/lib" psycopg2

'''