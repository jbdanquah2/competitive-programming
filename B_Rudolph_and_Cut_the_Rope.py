def minRopesToCut(n):
    count = 0

    for i in range(n):
        a, b = map(int, input().split()) 
        if b < a:
            count += 1
    return count

t = int(input())

for _ in range(t):
    n = int(input())
    print(minRopesToCut(n))
    
        