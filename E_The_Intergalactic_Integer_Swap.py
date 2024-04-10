from math import gcd

def calculate_max_gcd(n, coordinates):
    initial_gcd = coordinates[0]
    for i in range(1, n):
        initial_gcd = gcd(initial_gcd, coordinates[i])

    max_gcd = initial_gcd
    for factor in range(2, int(initial_gcd**0.5) + 1):
        if initial_gcd % factor == 0:
            max_gcd = max(max_gcd, factor)
            max_gcd = max(max_gcd, initial_gcd // factor)

    return max_gcd

# Input
n = int(input())
coordinates = list(map(int, input().split()))

# Calculate and output the maximum possible GCD after manipulation
result = calculate_max_gcd(n, coordinates)
print(result)
