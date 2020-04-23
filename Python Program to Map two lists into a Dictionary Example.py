# Python Program to Map two lists into a Dictionary

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)

********************************************************************************************
# Python Program to Map two lists into a Dictionary 2

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = dict(zip(keys, values))
print("Dictionary Items  :  ",  myDict)
