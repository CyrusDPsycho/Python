# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 09:09:38 2017

@author: CYRUS DSOUZA
"""
import fileinput
from sklearn.linear_model import LinearRegression

class PredictHousePrices: 
     
    
    def __init__(self):
        self.training_features = []
        self.training_class = []
        self.testing_features = [] 
        
    def filereader(self):
        i=-1
        for line in fileinput.input():
            
            if i==-1:
                rows = int(line.split(" ")[1])
                i=0
            elif i<rows:
                self.train(line,self.training_features,self.training_class)
                i+=1
            else:
                self.test(line,self.testing_features)
            
    def train(self,line,training_features,training_class):
        training_vector = [float(x) for x in line.split(" ")]
        training_features.append(training_vector[0:-1])
        training_class.append(training_vector[-1])
    
    def test(self,line,testing_features):
        testing_vector = [float(x) for x in line.split(" ")]
        if len(testing_vector)>1:
            testing_features.append(testing_vector)
    
        
    def predict(self,train_model,testing_features):
        prediction = train_model.predict(testing_features)
        for pred in prediction: 
            print pred
#---------------TEST BENCH-----------------------------

#    print "TEV",testing_vector #contains the test 
#    print "TEF",testing_features          

#    print "TV",training_vector  #training vector contains the line
#    print "TF",training_features #contains the training features 
#    print "TC",training_class #contains the trainee i.e price
 
            
predhp = PredictHousePrices()            
predhp.filereader()
train_model= LinearRegression().fit(predhp.training_features, predhp.training_class)           
predhp.predict(train_model,predhp.testing_features)