#Greatest Common Divisor a.k.a Highest Common Factor

n1 = (int)(input("Enter the first number :"))
n2 = (int)(input("Enter the second number :"))
smaller_of_two = 0
if n1 > n2:
    smaller_of_two = n2
else:
    smaller_of_two = n1
    
for i in range(1,smaller_of_two+1):
    if ((n1%i == 0) and (n2%i == 0)):
        gcd = i
print(gcd)