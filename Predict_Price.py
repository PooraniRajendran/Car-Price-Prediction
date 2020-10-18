# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:29:11 2020

@author: poora
"""

import pickle


class Predict_Price:
    def __init__(self):
        pass
    
    def predictCarPrice(self,data):
        model=pickle.load(open('RF_model.pkl','rb'))
        return model.predict([data])
        
