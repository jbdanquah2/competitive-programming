capacity = 0
sum = 0
n = int(input())
for i in range(n):
    total_a, total_b = map(int, input().split())
    sum -= total_a
    sum += total_b
    capacity = max(capacity, sum)

print(capacity)