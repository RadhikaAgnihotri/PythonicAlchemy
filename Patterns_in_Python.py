#To print 'n' number of *'s in a given line

num_of_stars = (int)(input("Enter the number of stars : "))
for i in range (num_of_stars): #range means (0,1,2,...(num_of_stars - 1))
    print('*', end=' ') #since default value of end operator is new line but we want in the same line so we replaced it with space
    
    