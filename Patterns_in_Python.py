#To print 'n' number of *s in a given line

num_of_stars = (int)(input("Enter the number of stars : "))
for i in range (num_of_stars): #range means (0,1,2,...(num_of_stars - 1))
    print('*', end=' ') #since default value of end operator is new line but we want in the same line so we replaced it with space

# #----------x----------x----------x----------x----------x----------x----------x----------    

# #Print a square pattern of 'n' number of *s in 'n' number of rows and columns[obviously]
# #1st approach
n = (int)(input("Enter the number of rows :"))
for j in range(n): #to iterate the above pattern like code for rows
    for i in range(n):
        print('*', end=' ')
    print(end='\n') #new line

# #2nd approach   
n1=(int)(input("Enter the number of rows :"))
for i in range(n1):
    print('* '*n1)   

#----------x----------x----------x----------x----------x----------

#Print a square pattern with an input digit eg.x, with x rows & columns[obviously]
#1st approach
n=(int)(input("Enter the digit :"))
for j in range(n):
    for i in range(n):
        print(n, end=' ')
    print(end='\n')  

#2nd approach
n1=(int)(input("Enter the digit :"))
for i in range(n1):
    print((str(n1)+' ')*n1) #newline is implicitly added by the print function. Each call to print outputs a new line by default, which is why you see the pattern in a square format

#----------x-----------x-----------x-----------x-----------x-----------x-----------x-----------x-----------

# 1 1 1 . . . 1[n times]
# 2 2 2 . . . 2 
# 3 3 3 . . . 3
# . . . . . . .
# n n n . . . n

n = (int)(input("Enter number of rows :"))
for i in range(n):
    print((str(i+1)+' ')*n) #adding 1 to i since it is an iterator that starts from 0
    
#----------x----------x----------x----------x----------x----------x----------

# A A A . . A[n times]
# A A A . . A
# . . . . .
# [n-1]th row of A
# A A A . . A

n = (int)(input("Enter the number of rows of the square :"))
for i in range(n):
    print(('A'+ ' ')*n) 
    #print('A '*n) #shorthand way of adding space
    
#----------x----------x----------x----------x----------x----------x----------x----------x----------

#To print pattern for example if n = 4
# A
# B B
# C C C
# D D D D

n = (int)(input("Enter the number of rows :"))
for i in range(n):
    print((chr(65+i)+' ')*(i+1)) #65 is ASCII value of capital A, end='\n' is done by default each time print function is called
    
#----------x----------x----------x----------x----------x----------x----------

#To print pattern for example if n = 4
# * * * *
# * * *
# * *
# *

#1st approach
n = (int)(input("Enter the number of rows :"))
for i in range(n):
    print(('* ')*n)
    n-=1 #just a shorthand notation of writing n = n - 1  

#2nd approach
n1 = (int)(input("Enter the number of rows :"))
for i in range(n1):
   print(('* ')*(n1-i))
  
