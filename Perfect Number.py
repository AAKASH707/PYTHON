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
