class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        player_distance = self.manhattan_distance((0, 0), target)

        for ghost in ghosts:

            ghost_distance = self.manhattan_distance(ghost, target)

            if ghost_distance <= player_distance:
                return False

        return True
    
    def manhattan_distance(self, p1, p2):

        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
