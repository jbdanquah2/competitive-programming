def solve(t, test_cases):
    results = []
    for s in test_cases:
        n = len(s)
        if n == 1:
            results.append("NO")
            continue
        
        # Sort the string to guarantee a different arrangement if needed
        sorted_s = sorted(s)
        
        # Perform a simple cyclic shift (rotate left)
        deranged_s = ''.join(sorted_s[1:] + sorted_s[:1])
        
        if deranged_s == s:
            results.append("NO")
        else:
            results.append("YES")
            results.append(deranged_s)
    
    return results

# Reading input
t = int(input().strip())
test_cases = [input().strip() for _ in range(t)]

# Solving the problem
results = solve(t, test_cases)

# Printing the results
for result in results:
    print(result)
