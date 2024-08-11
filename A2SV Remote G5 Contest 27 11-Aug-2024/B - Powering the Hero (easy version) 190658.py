# Problem: B - Powering the Hero (easy version) - https://codeforces.com/gym/541399/problem/B

import heapq

def max_army_power(t, cards):
    
    results = []
    
    bonus_deck = []
    total_power = 0
    
    for card in cards:
        if card > 0:
            heapq.heappush(bonus_deck, -card)  # push the negative to simulate max-heap
        elif bonus_deck:  # hero card and there's a bonus to use
            total_power += -heapq.heappop(bonus_deck)  # add the largest bonus

    
    return total_power

t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    # cases.append((n, cards))
    result = max_army_power(t, cards)
    print(result)
    
    


   
   
   
   
   