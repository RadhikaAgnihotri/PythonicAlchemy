#To print the alphabet A using '*' symbol

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

#Brute force approach
n = 7
for i in range(n):
    if i == 0:
        print('  '+'* '*3)
    if i == 1 or i == 2:
        print('* '+'  '*3+'* ')
    if i == 3:
        print('* '*5)
    if i == 4 or i == 5 or i == 6:
        print('* '+'  '*3+'* ')
        
#Systematic, thought through approach    
for row in range(7):
    for col in range(5):
        if (row == 0) and (col in {1,2,3}):
            print('*',end=' ')
        elif (row in {1,2,4,5,6}) and (col in {0,4}):
            print('*',end=' ')
        elif (row == 3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() #since next row will start in new line          