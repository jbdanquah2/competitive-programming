# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_almost_primes(n):
    # Step 1: Find all primes up to n using the Sieve of Eratosthenes
    is_prime = sieve_of_eratosthenes(n)
    
    # Step 2: Count distinct prime divisors for each number from 1 to n
    prime_divisors_count = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if is_prime[i]:  # If i is prime, mark its multiples
            for j in range(i, n + 1, i):
                prime_divisors_count[j] += 1
    
    # Step 3: Count how many numbers have exactly 2 distinct prime divisors
    almost_prime_count = 0
    for i in range(1, n + 1):
        if prime_divisors_count[i] == 2:
            almost_prime_count += 1
    
    return almost_prime_count

# Input reading
n = int(input())

# Output the result
print(count_almost_primes(n))
