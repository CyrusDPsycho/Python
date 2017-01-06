# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 10:59:44 2017

@author: CYRUS DSOUZA
"""

import fileinput

for line in fileinput.input():
    print line
    testing_data=float(line)
    print testing_data
    
'''
Based on the training data, we come to a conclusion that, when the battery
was charged for more than 4hours, it lasted 8hrs. Otherwise, just double.
'''

if testing_data>4:
    print 8
else:
    print 2*testing_data
    
'''
Always work on filtering and cleaning the data before working on it. 
Things are simpler that way and the output can be much organized
'''