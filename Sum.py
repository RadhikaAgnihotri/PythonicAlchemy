#Sum of odd-placed and even-placed digits

n = (int)(input("Enter a digit :"))
sum_odd = 0
sum_even = 0
for i in range(n):
    d = n % 10
    if i % 2 == 0:
        sum_even = sum_even + d
    else:
        sum_odd = sum_odd + d
    n = n // 10
print(sum_even)
print(sum_odd)
   
    