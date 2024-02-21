class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = [i for i in range(1, n + 1)]
        i = 0

        while len(friends) > 1:
            j = (i + k - 1) % len(friends)
        
            friends.pop(j)
            i = j

        return friends[0]
    