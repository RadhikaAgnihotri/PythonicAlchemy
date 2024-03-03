#To print the letter A using '*' symbol

#   * * *
# *       *
# *       *
# * * * * *
# *       *
# *       *
# *       *

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
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter B using '*' symbol

# * * * *
# *      *
# *      *
# * * * * 
# *      *
# *      *
# * * * *   

#1st approach
for row in range(7):
    for col in range(5):
        if row in {0,3,6} and col in {0,1,2,3}:
            print('*',end=' ')
        elif row in {1,2,4,5} and col in {0,4}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
   
#2nd approach
for row in range(7):
    for col in range(5):
        if row % 3 == 0 and col != 4:
            print('*', end=' ')  
        elif row % 3 != 0 and col % 4 == 0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()                        
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter C using '*' symbol

#   * * *
# *       *
# *      
# *  
# *      
# *       *
#   * * *   

for row in range(7):
    for col in range (5):
        if row in {0,6} and col in {1,2,3}:
            print('*',end = ' ')
        elif row in {1,5} and col in {0,4}:
            print('*',end = ' ')
        elif row in {2,3,4} and col == 0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 

#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter D using '*' symbol

# * * * *
# *       *
# *       *
# *       *
# *       *
# *       *
# * * * * 

for row in range(7):
    for col in range (5):
        if row in {0,6} and col != 4:
            print('*',end = ' ')
        elif row not in {0,6} and col in {0,4}:
            print('*',end = ' ')
        else:
            print(' ',end=' ')
    print()        
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter E using '*' symbol

# * * * * *
# *       
# *       
# * * * * *      
# *  
# *
# * * * * *

for row in range(7):
    for col in range (5):
        if row in {0,3,6}:
            print('*',end = ' ')
        elif row in {1,2,4,5} and col == 0:
            print('*',end = ' ')
        else:
            print(' ',end=' ')
    print() 
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter F using '*' symbol

# * * * * *
# *       
# *       
# * * * * *      
# *  
# *
# * 

for row in range(7):
    for col in range (5):
        if row in {0,3}:
            print('*',end = ' ')
        elif row not in {0,3} and col == 0:
            print('*',end = ' ')
        else:
            print(' ',end=' ')
    print()   

#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter G using '*' symbol

#   * * * 
# *       *  
# *       
# *   * * *      
# *       *
# *       *
#   * * * 

for row in range(7):
    for col in range (5):
        if row in {0,6} and col in {1,2,3}:
            print('*',end = ' ')
        elif row in {1,4,5} and col in {0,4}:
            print('*',end = ' ')
        elif row == 2 and col == 0:
            print('*', end=' ')
        elif row == 3 and col != 1:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print() 
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter H using '*' symbol

# *       *
# *       *  
# *       * 
# * * * * *     
# *       *
# *       *
# *       *

for row in range(7):
    for col in range (5):
        if row != 3 and col in {0,4}:
            print('*',end = ' ')
        elif row == 3:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print() 
    
#----------x----------x----------x----------x----------x----------x----------x----------

#To print the letter I using '*' symbol

# * * * * *       
#     *       
#     *       
#     *     
#     *       
#     *       
# * * * * *       

for row in range(7):
    for col in range (5):
        if row in {0,6}:
            print('*',end = ' ')
        elif row not in  {0,3} and col == 2:
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print() 
    
#----------x----------x----------x----------x----------x----------x----------x----------
        