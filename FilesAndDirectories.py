import os
import glob
import time 
#import humansize

print(os.path.join('D:\Python', 'Assignment1.py')) #join paths

print(os.path.expanduser('~')) #Expands all locations

os.chdir('D:/')
print(glob.glob('*D*.py'))    #LIKE Command in SQL.. Wildcard characters found


'''
	Information on when the file was last modified

'''


os.chdir('D:/Python')

print(os.getcwd())

metadata =  os.stat('sitemap.xml')
metadata.st_mtime #modified time from the os.stat() function

print(time.localtime(metadata.st_mtime)) #localtime converts the epoch time into current format

print(metadata.st_size) #size of the data file. 

#print(humansize.approximate_size(metadata.st_size)) #Converts it to readable human size format


'''
Constructing Absolute Pathnames
'''

print(os.path.realpath('sitemap.xml')) #Gives you the path all the way from the root directory




