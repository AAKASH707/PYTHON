# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)

*******************************************************************************************************

  *** Python Program to Calculate Sum of Arithmetic Progression Series without Math Formula  ***

  # Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = 0
value = a
print("Arithmetic Progression Series : ", end = " ")
for i in range(n):
    print("%d + " %value, end = " ")
    total = total + value
    value = value + d

print("\nThe Sum of Arithmetic Progression Series upto %d = %d " %(n, total))

*******************************************************************************************************
     ***  Python Program to Calculate Sum of Arithmetic Progression Series using Functions  ***

     # Python Program to find Sum of Arithmetic Progression Series

def sumofAP(a, n, d):
    total = (n * (2 * a + (n - 1) * d)) / 2
    return total

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = sumofAP(a, n, d)
print("\nThe Sum of Arithmetic Progression Series = " , total) 

*******************************************************************************************************


