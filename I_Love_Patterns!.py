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


        