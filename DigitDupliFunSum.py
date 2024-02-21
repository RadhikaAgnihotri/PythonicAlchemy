#Accept integer n, and print value of n+nn+nnn

n = int(input("Enter a number :"))
sum = 0
for i in range(n):
    sum = ((1*n)+(11*n)+(111*n))
print(sum)

# Accept an integer N
N = int(input())

# Calculate the value of N+NN+NNN
result = N + int(str(N) * 2) + int(str(N) * 3)

# Display the result
print(result)