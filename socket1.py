import urlib
from BeautifulSoup import *

url = raw_input('Enter -')

html = urllib.urlopen(http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html).read()
soup = BeautifulSoup(html)

#Retrieve the list of span tags
#Sum of all the numbers in them.

tags = soup('a')

for tag in tags:
    print tag.get('href',None)
