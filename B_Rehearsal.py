
def minimumAmountOfTime(n, pairs):
    pairs.sort(key=lambda x: x[1])
    time = 0
   
    for i in range(n // 2):
        time += pairs[i][1] + pairs[len(pairs) - i - 1][1]
        return time

    
n = int(input())
pairs = []
for _ in range(n):
    x, y = map(int, input().split())
    pairs.append((x,y))
print(minimumAmountOfTime(n, pairs))

