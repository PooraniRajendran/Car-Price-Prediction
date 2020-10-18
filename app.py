# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:09:01 2020

@author: poora
"""
from flask import Flask, render_template,request
from Predict_Price import Predict_Price
app=Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':
        Present_Price=float(request.form['Present_Price'])
        
        Fuel_Type=request.form['Fuel_Type']
        Fuel_Type_Petrol=0
        if(Fuel_Type=='Petrol'):
            Fuel_Type_Petrol=1
        
        Seller_Type=request.form['Seller_Type']
        Seller_Type_Individual=0
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
        
        Transmission_Manual=request.form['Transmission_Mannual']
        Transmission_Manual=0
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
        
        num_years=2020-(int(request.form['Year']))
        
        data=[Present_Price,Fuel_Type_Petrol,Seller_Type_Individual,
        Transmission_Manual,num_years]
        
        print("before class instantiation")
        pred_class=Predict_Price()
        print("after class instantiation and before prediction call")
        prediction=pred_class.predictCarPrice(data)
        print("after prediction call")
        predicted_price=round(prediction[0],2)
        
        if predicted_price<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell this car is {}".format(predicted_price))
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)