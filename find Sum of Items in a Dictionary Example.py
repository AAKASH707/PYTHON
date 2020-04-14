# Python Program to find Sum of Items in a Dictionary

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)

# Print Values using get
print("\nSum of Values: ", sum(myDict.values()))
*******************************************************************************************************
                                 # Python Program to find Sum of Items in a Dictionary Example 2

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)
total = 0

# Print Values using get
for i in myDict.values():
    total = total + i
    
print("\nThe Total Sum of Values : ", total)
