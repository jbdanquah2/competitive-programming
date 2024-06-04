def minimal_operations(a, m):
    # Initialize an array to store the minimum number of operations for each value of a
    dp = [float('inf')] * (a + 1)
    dp[0] = 0

    # Calculate the minimum operations for each value of a
    for i in range(1, a + 1):
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i >= 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)

    # Check if the total number of operations is a multiple of m
    if dp[a] % m == 0:
        return dp[a]
    else:
        return -1

# Example usage
a, m = map(int, input().split())
result = minimal_operations(a, m)
print(result)
