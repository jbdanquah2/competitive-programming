# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        if not coins:
            return -1

        # Initialize the queue for BFS
        queue = deque([(0, 0)])  # (current amount, number of coins)
        visited = set()  # To keep track of visited amounts

        while queue:
            current_amount, num_coins = queue.popleft()

            for coin in coins:
                next_amount = current_amount + coin
                if next_amount == amount:
                    return num_coins + 1
                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))

        return -1
        

        

        