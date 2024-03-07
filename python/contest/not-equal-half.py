def solve(n, arr):
    arr.sort()
    if arr[:n] == arr[n:]:
        return -1
    return arr

if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))

    result = solve(n, arr)

    if result == -1:
        print(-1)
    else:
        print(*result)
