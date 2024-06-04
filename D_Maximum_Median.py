n, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, len(a) - 1
# 1 3 5
while left <= right:
    mid = left + (right - left) // 2

    median = a[mid]




print(median)
