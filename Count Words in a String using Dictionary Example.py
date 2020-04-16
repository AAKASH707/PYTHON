# Python Program to Count words in a String using Dictionary

string = input("Please enter any String : ")
words = []

words = string.split()
frequency = [words.count(i) for i in words]

myDict = dict(zip(words, frequency))
print("Dictionary Items  :  ",  myDict)
