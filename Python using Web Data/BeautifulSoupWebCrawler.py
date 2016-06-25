import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter-')
global position,crawl_counter,counter,count

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
position =int(raw_input("Enter the position to crawl into: "))
count = int(raw_input("Enter the number of web crawls"))
print "Retrieving: ",url
counter,crawl_counter,flag = 0,2,False

tags = soup('a')

#Retrieve the list of anchor tags
#Crawl function to crawl through the desired webpages with the position and count taken..

def crawler(chtml):
    
    global position,counter,crawl_counter,flag
    csoup = BeautifulSoup(chtml)
    atag = csoup('a')
    counter = 0
    
  

    for link in atag:
        crawled_url = link.get('href',None)
        counter += 1
        if(crawl_counter == count): 
            flag = True
        if(counter == position):
            crawlHtml= urllib.urlopen(crawled_url).read()
            crawl_counter += 1
            if(flag):
                print "Last Url: ",crawled_url
                return
            else:
                print "Retrieving: ",crawled_url
                crawler(crawlHtml)
        
        

for tag in tags:
    crawler_url = tag.get('href',None)
    counter +=1
    
    if(counter==position):
        print 'Retrieving:',crawler_url
        crawler_html = urllib.urlopen(crawler_url).read()
        crawler(crawler_html)
