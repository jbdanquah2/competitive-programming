def z_sort(n, arr):
    arr.sort()
    result = []
    mid = n // 2
    for i in range(mid):
        result.append(arr[i])
        result.append(arr[n - i - 1])
    if n % 2 == 1:
        result.append(arr[mid])

    return result


n = int(input())
arr = list(map(int, input().split()))

res = z_sort(n, arr)
print(*res)
