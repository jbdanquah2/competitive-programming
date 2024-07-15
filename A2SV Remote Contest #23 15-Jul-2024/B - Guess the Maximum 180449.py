# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

def find_maximum_k(t, n, arr):
   
    max_k = float('inf')
    
    for i in range(1, n):
        max_k = min(max_k, max(arr[i-1], arr[i]))
    
    return max_k-1

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    results.append(find_maximum_k(t, n, arr))

for result in results:
    print(result)
