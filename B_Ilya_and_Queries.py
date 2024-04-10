def count_consecutive_chars(s):
    n = len(s)
    prefix_sum = [0] * n
    count = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        prefix_sum[i] = count

    return prefix_sum

def solve_queries(s, queries):
    prefix_sum = count_consecutive_chars(s)
    result = []

    for query in queries:
        li, ri = query
        result.append(prefix_sum[ri - 1] - prefix_sum[li - 1])

    return result

# Input parsing
s = input().strip()
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

# Solve queries and print results
result = solve_queries(s, queries)
for r in result:
    print(r)
