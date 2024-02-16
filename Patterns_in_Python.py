#To print 'n' number of *s in a given line

num_of_stars = (int)(input("Enter the number of stars : "))
for i in range (num_of_stars): #range means (0,1,2,...(num_of_stars - 1))
    print('*', end=' ') #since default value of end operator is new line but we want in the same line so we replaced it with space

#----------x----------x----------x----------x----------x----------x----------x----------    

#Print a square pattern of 'n' number of *s in 'n' number of rows and columns[obviously]
#1st approach
n = (int)(input("Enter the number of rows :"))
for j in range(n): #to iterate the above pattern like code for rows
    for i in range(n):
        print('*', end=' ')
    print(end='\n') #new line

#2nd approach   
n1=(int)(input("Enter the number of rows :"))
for i in range(n1):
    print('* '*n1)   

#----------x----------x----------x----------x----------x----------

 