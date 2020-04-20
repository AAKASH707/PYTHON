# Python Program to Create Dictionary of Numbers 1 to n in (x, x*x) form

number = int(input("Please enter the Maximum Number : "))

myDict = {x:x * x for x in range(1, number + 1)}

print("\nDictionary = ", myDict)
