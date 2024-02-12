class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """

        seen_both = set()
        min_num = float('inf')

        for front, back in zip(fronts, backs):
            if front == back:
                seen_both.add(front)

        for num in fronts + backs:
            if num not in seen_both:
                min_num = min(min_num, num)

        return min_num if min_num != float('inf') else 0
    


        