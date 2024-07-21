# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

def main(potions: list) -> int: 
    
    current_health = 0
    count = 0
    min_heap = []

    for i in range(n):
        potion = potions[i]
        
        if potion >= 0:
            current_health += potion
            count += 1
        else:
            if current_health + potion >= 0:
                current_health += potion
                count += 1
                heapq.heappush(min_heap, potion)
            else:
                if min_heap and min_heap[0] < potion:
                    current_health += potion - heapq.heappop(min_heap)
                    heapq.heappush(min_heap, potion)
    
    return count

n = int(input())
arr = list(map(int, input().split()))
print(main(arr))

