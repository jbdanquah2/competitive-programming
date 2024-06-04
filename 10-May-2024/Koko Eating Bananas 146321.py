# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Define a function to check if it's possible to eat all bananas within h hours
        def canEatAll(speed):
            hours = 0
            for bananas in piles:
                hours += (bananas + speed - 1) // speed  # Round up division to get hours needed for each pile
            return hours <= h
        
        # Binary search for the minimum k
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        return left




            