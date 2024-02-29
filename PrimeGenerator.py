#Generate prime numbers for a given number of test cases
#where each case consists of two numbers[m,n] 
#output all prime numbers p in range [m <= p <= n]

def generate_primes(m, n):
    primes = []
    for num in range(max(2, m), n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def main():
    t = int(input("Enter the number of test cases: "))
    test_cases = []
    for _ in range(t):
        m, n = map(int, input().split())
        test_cases.append((m, n))

    for m, n in test_cases:
        primes = generate_primes(m, n)
        print(" ".join(map(str, primes)))

if __name__ == "__main__":
    main()