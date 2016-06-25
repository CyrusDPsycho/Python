# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:12:58 2015

@author: CyrusDPsycho
"""

import json
import urllib 

url = raw_input("Enter location")
print 'Retreiving' + url 
uh = urllib.urlopen(url)
data = uh.read()

info = json.loads(data)
for item in info:
    print item['note']
        
        