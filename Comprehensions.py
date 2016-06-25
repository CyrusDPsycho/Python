'''
List comprehensions
'''

a = [2,4,3,3,5,3,2,4]

print([elem for elem in a]) #List comprehension technique

'''
Using list comprehensions for files and their directories

'''

import os, glob

print(glob.glob('*map*.xml'))

print([os.path.realpath(f) for f in glob.glob('*map*.xml')])

print([f for f in glob.glob('*.py') if os.stat(f).st_size < 6000])

#Gets the path of the file and the size of the file
print([(os.path.realpath(f), os.stat(f).st_size) for f in glob.glob('*map*.xml')])


'''

Dictionary Comprehensions

'''
print('')
metadata = [(f,os.stat(f)) for f in glob.glob('*.py')]
print(metadata[0])

metadata_dict = {f : os.stat(f) for f in glob.glob('*.py')}
print('')
D = list(metadata_dict.keys())

print(D[0],metadata_dict['ListComprehensions.py'].st_size)

'''

Dictionary Swapping Technique Comprehension

'''

a_dict = {1:'a', 2: 'b', 4: 'c'}

print(a_dict)
print({value : key  for key,value in a_dict.items()})


