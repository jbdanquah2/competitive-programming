# Problem: B - Chef Jamie - https://codeforces.com/gym/537575/problem/B

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    ordered = sorted(arr)
    swaps = 0
    
    for i in range(n):
        if arr[i] != ordered[i]:
            swaps += 1

    print(max(0, swaps - 1))


if __name__ == "__main__":
    solve()
    