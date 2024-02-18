N = int(input())
a = input().split()
b = input().split()
c = input().split()

a = list(map(int, a))
b = list(map(int, b))
c = list(map(int, c))

count = 0
for i in range(N):
    
    for j in range(N):
        cj = c[j]
        
        if cj >= N:
            continue
        
        if a[i] == b[cj]:
            count += 1
           
print(count)
