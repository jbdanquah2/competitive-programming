# Problem: A - My First Sorting Problem - https://codeforces.com/gym/541399/problem/A


def main(arr: list) -> list:
    
    if not arr:
        return []
    
    a = arr[0]
    b = arr[1]
    
    if a < b:
        return [a, b]
    else:
        return [b, a]
   
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    result = main([a, b])
    print(*result)
    