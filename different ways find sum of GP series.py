# Python Program to find Sum of Geometric Progression Series
import math

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = (a * (1 - math.pow(r, n ))) / (1- r)
tn = a * (math.pow(r, n - 1))

print("\nThe Sum of Geometric Progression Series = " , total)
print("The tn Term of Geometric Progression Series = " , tn)

**************************************************************************************************************************

                   *** Program to find Sum of Geometric Progression Series without Math Formula ****
                   
# Python Program to find Sum of Geometric Progression Series

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = 0
value = a
print("\nG.P  Series :", end = " ")
for i in range(n):
    print("%d  " %value, end = " ")
    total = total + value
    value = value * r
    
print("\nThe Sum of Geometric Progression Series = " , total)

*******************************************************************************************************************

           ****  Python Program to Calculate Sum of Geometric Progression Series using Functions ****
           
 # Python Program to find Sum of Geometric Progression Series
import math

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    return total

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = sumofGP(a, n, r)
print("\nThe Sum of Geometric Progression Series = " , total)
