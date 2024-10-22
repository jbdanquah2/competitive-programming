# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

def gcd_of_range(a, b):
    if a == b:
        return a
    else:
        return 1

# Input reading
a, b = input().split()

# Output the result
print(gcd_of_range(a, b))
