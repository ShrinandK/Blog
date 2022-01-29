from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
swagger = Swagger(app)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict',methods=['Get'])
@swag_from('getdata.yml')
def predictHousingPrice():    
    
    area = request.args.get("area")
    bedroom = request.args.get("bedroom")
    bath = request.args.get("bath")    
    Locality1 = request.args.get("Locality1")
    Locality2 = request.args.get("Locality2")
    Locality3 = request.args.get("Locality3")
    Locality4 = request.args.get("Locality4")
    prediction = classifier.predict([[area,bedroom,bath,Locality1,Locality2,Locality3,Locality4]])
    print(prediction)
    return "The estimated price is " + str(prediction) + "lakhs."          

if __name__=='__main__':
    app.run()