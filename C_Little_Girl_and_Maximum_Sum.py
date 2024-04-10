
n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# Initialize the prefix sum array
prefix_sum = [0] * (n + 1)
for i in range(0, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

# Process each query
max_sum = 0
for _ in range(q):
    l, r = map(int, input().split())
    max_sum += prefix_sum[r] - prefix_sum[l-1]

print(max_sum)
