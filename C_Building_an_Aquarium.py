def maxHeightOfTankRequired(n, x, arr):
    left, right = 1, max(arr) + x  # Generously set the upper bound

    while left < right:
        mid = (left + right + 1) // 2
        water_needed = sum(max(0, mid - height) for height in arr)

        if water_needed <= x:
            left = mid
        else:
            right = mid - 1

    return left


t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxHeightOfTankRequired(n, x, arr))
