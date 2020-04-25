# Python Program to Multiply All Items in a Dictionary

myDict = {'x': 20, 'y':5, 'z':60}
print("Dictionary: ", myDict)

total = 1
# Multiply Items
for key in myDict:
    total = total * myDict[key]
    
print("\nAfter Multiplying Items in this Dictionary: ", total)
