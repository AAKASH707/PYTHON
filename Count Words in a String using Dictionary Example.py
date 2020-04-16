# Python Program to Count words in a String using Dictionary

string = input("Please enter any String : ")
words = []

words = string.split()
frequency = [words.count(i) for i in words]

myDict = dict(zip(words, frequency))
print("Dictionary Items  :  ",  myDict)

***********************************************************************************************
# Python Program to Count words in a String using Dictionary 2

string = input("Please enter any String : ")
words = []

words = string.split() # or string.lower().split()
myDict = {}
for key in words:
    myDict[key] = words.count(key)

print("Dictionary Items  :  ",  myDict)
