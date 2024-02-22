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
      
        