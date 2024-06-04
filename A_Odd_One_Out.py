def occursOnce(arr):
    left, right = 0, len(arr) - 1

    mid = left + (right - left) // 2

    if arr[mid] == arr[mid + 1]:
        return arr[mid - 1]
    elif arr[mid] == arr[mid - 1]:
        return arr[mid + 1]
    else:
        return arr[mid]


n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    print(occursOnce(arr))