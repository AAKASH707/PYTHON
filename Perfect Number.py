# Python Program to find Perfect Number using For loop

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)
******************************************************************************************************************************
                                                    // Perfect Number using While Loop
# Python Program to find Perfect Number using While loop

Number = int(input(" Please Enter any Number: "))
i = 1
Sum = 0
while(i < Number):
    if(Number % i == 0):
        Sum = Sum + i
    i = i + 1
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not the Perfect Number" %Number)                                                    
*******************************************************************************************************************************
                                            // Perfect Number using Function
    # Python Program to find Perfect Number using Functions

def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    return Sum        

# Taking input from the user
Number = int(input("Please Enter any number: "))
if (Number == Perfect_Number(Number)):
    print("\n %d is a Perfect Number" %Number)
else:
    print("\n %d is not a Perfect Number" %Number)
*****************************************************************************************************************************
                                           // Program to Find Perfect Number between 1 to 1000
    # Python Program to find Perfect Number between 1 to 1000

# Taking input from the user
Minimum = int(input("Please Enter any Minimum Value: "))
Maximum = int(input("Please Enter any Maximum Value: "))

# initialise sum


# Checking the Perfect Number
for Number in range(Minimum, Maximum - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n       
    # display the result
    if(Sum == Number):
        print(" %d " %Number)
