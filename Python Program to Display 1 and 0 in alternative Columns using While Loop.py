# Python Program to Print 1 and 0 in alternative Columns
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative Columns")
i = 1
while(i <= rows):
    j = 1
    while(j <= columns):
        if(j % 2 != 0):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
        j = j + 1
    i = i + 1
    print()
