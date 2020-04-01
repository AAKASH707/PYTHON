# Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
***********************************************************************************************************************
                             Python Program to Print Hollow Square of Stars using While Loop
                             
 # Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
i = 0
while(i < side):
    j = 0
    while(j < side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()
