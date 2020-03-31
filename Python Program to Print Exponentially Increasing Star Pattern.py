# Python Program to Print Exponentially Increasing Star Pattern
import math

rows = int(input("Please Enter the total Number of Rows  : "))

print("Exponentially Increasing Stars") 
i = 0
while(i <= rows):
    j = 1
    while(j <= math.pow(2, i)):        
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()
