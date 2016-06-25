# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 04:54:51 2015

@author: CyrusDPsycho
"""

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_192417.xml'

uh = urllib.urlopen(url)
print 'Retrieving', url
data = uh.read()
isum = 0
tree = ET.fromstring(data)

s = tree.findall(".//count")  

for item in s: 
    isum += int(item.text)
    
print isum

