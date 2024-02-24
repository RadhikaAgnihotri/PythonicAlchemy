#To print the pattern, for example if n=5
# 5
# 3
# 1
# 2
# 4

#Explanation: The pattern prints odd numbers uptil n in descending order and the even numbers till n in ascending order

n = (int)(input("Enter a number :"))
#To print odd digits in descending order
for i in range(n,0,-1): #range[start,stop[not included],step]
    if i%2 != 0:
        print(i)

#To print even numbers in ascending order        
for i in range(2,n+1,2):
    if i%2 == 0:
        print(i)
        
#----------x----------x-----------x-----------x-----------x-----------x-----------x-----------

#To print the pattern, example if n=5
# A
# A B
# A B C
# A B C D
# A B C D E

n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j)+' ',end='')
    print() 
    
#----------x----------x----------x----------x----------x----------x

#To print a pattern, example if n=4
# 4
# 4 3
# 4 3 2
# 4 3 2 1

n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(i+1):
        print(chr(48+n-j)+' ',end='') #print(n-j,end='') another way
    print() 
           
#----------x----------x----------x----------x----------x----------x   

#To print the pattern, example if n=4
# D
# D C 
# D C B 
# D C B A

n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()
        
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
# A A A A
# B B B 
# C C  
# D 

n = (int)(input("Enter a number :"))
for i in range(n):
    print((chr(65+i)+' ')*(n-i))
           
#----------x----------x----------x----------x----------x----------x       

#To print the pattern, example if n=4
# 4 4 4 4
# 3 3 3 
# 2 2  
# 1

n = (int)(input("Enter a number :"))
for i in range(n):
    #print((chr(48+n-i)+' ')*(n-i)) 
    print((str(n-i)+' ')*(n-i)) #for '+' operator, both args should be str
    
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
# D D D D
# C C C 
# B B  
# A

n = (int)(input("Enter a number :"))
for i in range(n):
    print((chr(64+n-i)+' ')*(n-i))
           
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
# A B C D
# A B C 
# A B  
# A

n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(n-i):
        print((chr(65+j)+' '),end='')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
# 4 3 2 1
# 4 3 2 
# 4 3  
# 4

n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(n-i):
        print((chr(48+n-j)+' '),end='')
        #print(n-j,end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
# D C B A
# D C B 
# D C  
# D

n = (int)(input("Enter a number :"))
for i in range(n): #row loop
    for j in range(n-i): #column loop
        print((chr(64+n-j)+' '),end='')
        #print(chr(64+n-j),end=' ')
    print()
       
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
#    1 
#   1 2 
#  1 2 3   
# 1 2 3 4 

n = int(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(49+j)+' ',end='')
        #print(j+1,end=' ')
    print() 
           
#----------x----------x----------x----------x----------x----------x

#To print the pattern, example if n=4
#    A  
#   A B 
#  A B C   
# A B C D 

n = int(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print() 
           
#----------x----------x----------x----------x----------x----------x 

#To print the pattern, example if n=4
#    4  
#   4 3 
#  4 3 2   
# 4 3 2 1 

n = int(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(48+n-j),end=' ')
        #print(n-j,end=' ')
    print()
          
#----------x----------x----------x----------x----------x----------x

#Accept an integer n, and print value of n+nn+nnn

#Logic if pattern only sticks to n+nn+nnn
n = int(input())
sum = 0
for i in range(n):
    sum = ((1*n)+(11*n)+(111*n))
print(sum)

#Logic if pattern
# Accept an integer N
N = int(input())

# Calculate the value of N+NN+NNN
result = N + int(str(N) * 2) + int(str(N) * 3)

# Display the result
print(result)   
    
#----------x----------x----------x----------x----------x----------x

#To print an inverted pyramid, if n=4
# * * * *
#  * * *
#   * *
#    *

n = (int)(input("Enter a number :"))
for i in range(n):
    print((' '*(i))+('* '*(n-i)))
           
#----------x----------x----------x----------x----------x----------x

#To print an inverted pyramid, if n=4
# 1 1 1 1
#  2 2 2
#   3 3
#    4

n = (int)(input("Enter a number :"))
for i in range(n):
    print((' '*(i))+((chr(49+i)+' ')*(n-i)))
    #print(' '*i+(str(i+1)+' ')*(n-i))
           
#----------x----------x----------x----------x----------x----------x

#To print an inverted pyramid, if n=4
# A A A A
#  B B B
#   C C
#    D

n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*i+(chr(65+i)+' ')*(n-i))
           
#----------x----------x----------x----------x----------x----------x

#To print an inverted pyramid, if n=4
# 1 2 3 4
#  1 2 3
#   1 2
#    1

n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(chr(49+j)+' ',end='')
        #print(j+1,end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x 

#To print an inverted pyramid, if n=4
# A B C D
#  A B C
#   A B
#    A

n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()
          
#----------x----------x----------x----------x----------x----------x

#To print an inverted pyramid, if n=4
# 4 3 2 1
#  4 3 2
#   4 3
#    4

n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(chr(48+n-j),end=' ')
        #print(n-j,end=' ')
    print() 
           
#----------x----------x----------x----------x----------x----------x 

#To print an inverted pyramid, if n=4
# D C B A
#  D C B
#   D C
#    D

n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(chr(64+n-j),end=' ')
    print() 
          
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

#1st method
n = (int)(input("Enter a number :"))
for i in range(n-1):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print('* ',end='')
    print()    
for i in range(n):
    print(' '*(i),end='')
    for j in range(n-i):
        print('* ',end='')
    print()    
  
#2nd method/concise
n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))
print()
       
#----------x----------x----------x----------x----------x----------x 

#To print a diamond, if n=4
#    1
#   2 2
#  3 3 3
# 4 4 4 4
#  3 3 3
#   2 2
#    1

#1st method
n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print((i+1),end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print((n-i-1),end=' ')
    print()    
  
#2nd method/concise
n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
for i in range(n-1):
    print(' '*(i+1)+(str(n-i-1)+' ')*(n-i-1))
          
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    A 
#   B B
#  C C C
# D D D D
#  C C C
#   B B
#    A

#1st method
n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(63+n-i),end=' ')
    print()    
  
#2nd method/concise
n = (int)(input("Enter a number :"))
for i in range(n):
    print(' '*(n-i-1)+(chr(65+i)+' ')*(i+1))
for i in range(n-1):
    print(' '*(i+1)+(chr(63+n-i)+' ')*(n-i-1))
       
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    1 
#   1 2
#  1 2 3
# 1 2 3 4
#  1 2 3
#   1 2
#    1

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(49+j),end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(49+j),end=' ')
    print()    
           
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    A 
#   A B
#  A B C
# A B C D
#  A B C
#   A B
#    A

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    4 
#   4 3
#  4 3 2
# 4 3 2 1
#  4 3 2
#   4 3
#    4

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(48+n-j),end=' ')
        #print(n-j,end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(48+n-j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print a diamond, if n=4
#    D 
#   D C
#  D C B 
# D C B A
#  D C B
#   D C
#    D

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond i.e. pyramid
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
        #print(n-j,end=' ')
    print()    
for i in range(n-1): #2nd half of diamond i.e. inverted pyramid
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print a half diamond, if n=4
# 1 
# 2 2
# 3 3 3 
# 4 4 4 4
# 3 3 3
# 2 2
# 1  

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond 
    print((chr(49+i)+' ')*(i+1))
    #print((str(i+1)+' ')*(i+1))
for i in range(n-1):
    print((chr(47+n-i)+' ')*(n-i-1))
    #print((str(n-i-1)+' ')*(n-i-1))
           
#----------x----------x----------x----------x----------x----------x

#To print a half diamond, if n=4
# A 
# B B
# C C C 
# D D D D
# C C C
# B B
# A  

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond 
    print((chr(65+i)+' ')*(i+1))
for i in range(n-1):
    print((chr(63+n-i)+' ')*(n-i-1))
           
#----------x----------x----------x----------x----------x----------x

#To print a half diamond, if n=4
# 4   
# 4 3
# 4 3 2  
# 4 3 2 1
# 4 3 2
# 4 3
# 4   

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond 
    for j in range(i+1):
        print(n-j,end=' ')
    print()    
for i in range(n-1):
    for j in range(n-i-1):
        print(n-j,end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print a half diamond, if n=4
# D   
# D C
# D C B  
# D C B A
# D C B
# D C
# D   

n = (int)(input("Enter a number :"))
for i in range(n): #1st half of diamond 
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()    
for i in range(n-1): #2nd half of diamond
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
#       *  
#     * *
#   * * *  
# * * * *
#   * * *
#     * *
#       *  

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+'* '*(i+1)) #2 spaces i.e. the space b/w 2 spaces
   
for i in range(n-1): 
    print('  '*(i+1)+'* '*(n-i-1)) #2 spaces i.e. space symbol followed by space separator
         
#----------x----------x----------x----------x----------x----------x 

#To print left half of diamond, if n=4
#       1  
#     2 2
#   3 3 3  
# 4 4 4 4
#   3 3 3
#     2 2
#       1  

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+(str(i+1)+' ')*(i+1))
for i in range(n-1): 
    print('  '*(i+1)+(str(n-i-1)+' ')*(n-i-1)) 
          
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
# 1***  
# 12**
# 123* 
# 1234
 
n = (int)(input("Enter a number :"))
for i in range(n):
    for j in range(i+1):
        print(str(j+1),end='')
    print('*'*(n-i-1))
       
#----------x----------x----------x----------x----------x----------x 

#To print left half of diamond, if n=4
#       A
#     B B 
#   C C C 
# D D D D
#   C C C
#     B B
#       A
 
n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+(chr(65+i)+' ')*(i+1))
    #print()    
for i in range(n-1):
    print('  '*(i+1)+(chr(63+n-i)+' ')*(n-i-1)) 
         
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
#       1
#     1 2 
#   1 2 3 
# 1 2 3 4
#   1 2 3
#     1 2
#       1
 
n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(j+1,end=' ')
    print()    
for i in range(n-1):
    print('  '*(i+1),end='')
    for j in range(n-i-1):
        print(j+1,end=' ')
    print()    
       
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
#       A 
#     A B
#   A B C
# A B C D
#   A B C
#     A B
#       A
 
n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()    
for i in range(n-1):
    print('  '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
#       4 
#     4 3
#   4 3 2
# 4 3 2 1
#   4 3 2
#     4 3
#       4
 
n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(n-j,end=' ')
    print()    
for i in range(n-1):
    print('  '*(i+1),end='')
    for j in range(n-i-1):
        print(n-j,end=' ')
    print() 
           
#----------x----------x----------x----------x----------x----------x

#To print left half of diamond, if n=4
#       D 
#     D C
#   D C B
# D C B A
#   D C B
#     D C
#       D
 
n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()    
for i in range(n-1):
    print('  '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print top half hollow diamond with *, if n=4
#       ** 
#     *    *
#   *        *
# *            *

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(2):
        print('*',end='')
        print('    '*(i),end='')
    print()    
           
#----------x----------x----------x----------x----------x----------x

#To print top half hollow diamond with *, if n=4
#       * 
#     *   *
#   *       *
# *           *

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+'* ',end='')
    if i >= 1:
        print('  '*(2*i-1)+'*',end='')
    print() 
           
#----------x----------x----------x----------x----------x----------x

#To print top half hollow diamond, if n=4
#       1 
#     2   2
#   3       3
# 4           4

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+str(i+1),end=' ')
    if i >= 1:
        print('  '*(2*i-1)+str(i+1),end='') #spaces b/w the digits = [2i-1]
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print top half hollow diamond, if n=4
#       A 
#     B   B
#   C       C
# D           D

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+chr(65+i),end=' ')
    if i >= 1:
        print('  '*(2*i-1)+chr(i+65),end='') 
    print() 
           
#----------x----------x----------x----------x----------x----------x 

#To print top half hollow diamond, if n=4
#       4 
#     3   3
#   2       2
# 1           1

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+str(n-i),end=' ')
    if i >= 1:
        print('  '*(2*i-1)+str(n-i),end='') 
    print() 
          
#----------x----------x----------x----------x----------x----------x 

#To print top half hollow diamond, if n=4
#       D 
#     C   C
#   B       B
# A           A

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(n-i-1)+chr(64+n-i),end=' ')
    if i >= 1:
        print('  '*(2*i-1)+chr(64+n-i),end='') 
    print() 
          
#----------x----------x----------x----------x----------x----------x

#To print bottom half hollow diamond, if n=4
# *           *       
#   *       *
#     *   *
#       *

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(i)+'* ',end='')
    if i != (n-1): #means except last row
        print('  '*(2*n-2*i-3)+'*',end='') #spaces b/w 2 stars = [2n-2i-3]
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print bottom half hollow diamond, if n=4
# 4           4       
#   3       3
#     2   2
#       1

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(i)+str(n-i)+' ',end='')
    if i != (n-1): 
        print('  '*(2*n-2*i-3)+str(n-i),end='') 
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print bottom half hollow diamond, if n=4
# D           D       
#   C       C
#     B   B
#       A

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(i)+chr(64+n-i),end=' ')
    if i != (n-1): 
        print('  '*(2*n-2*i-3)+chr(64+n-i),end='') 
    print()
           
#----------x----------x----------x----------x----------x----------x

#To print bottom half hollow diamond, if n=4
# 1           1       
#   2       2
#     3   3
#       4

n = (int)(input("Enter a number :"))
for i in range(n):
    print('  '*(i)+str(i+1),end=' ')
    if i != (n-1): 
        print('  '*(2*n-2*i-3)+str(i+1),end='') 
    print()
           
#----------x----------x----------x----------x----------x----------x       
      
        