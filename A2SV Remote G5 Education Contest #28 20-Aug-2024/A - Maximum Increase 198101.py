# Problem: A - Maximum Increase - https://codeforces.com/gym/543262/problem/A


def main(n, arr: list) -> int:
    if n == 0:
        return 0

  
    dp = [1] * (n+1)

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1

    return max(dp)

n = int(input())
arr = list(map(int, input().split()))

print(main(n, arr))
