# Problem: B - Remove Smallest - https://codeforces.com/gym/536373/problem/B


def main(arr: list)-> str: 
    arr.sort()
    for i in range(1, len(arr)): 
        if arr[i] - arr[i-1] > 1: 
            return 'NO'
    return 'YES'

t = int(input())
for _ in range(t): 
    n = int(input())
    arr = list(map(int, input().split()))
    print(main(arr))
