# Python Program to Map two lists into a Dictionary

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)
