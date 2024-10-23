# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
    
        # Initialize an array to track prime numbers
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False  # 0 and 1 are not prime numbers
        
        # Apply the Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        # Count the number of prime numbers
        return sum(isPrime)
            