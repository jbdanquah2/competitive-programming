# Problem: D - Firaol And His Weapon - https://codeforces.com/gym/541399/problem/D

def max_resources(n, masses):
    max_mass = max(masses)
    
    frequency = [0] * (max_mass + 1)
    for mass in masses:
        frequency[mass] += 1
    
    dp = [0] * (max_mass + 1)
    
    dp[1] = frequency[1] * 1
    
    for i in range(2, max_mass + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * frequency[i])
    
    return dp[max_mass]

n = int(input())
masses = list(map(int, input().split()))
print(max_resources(n, masses))
