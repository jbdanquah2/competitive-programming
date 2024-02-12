class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        n = len(boxes)
        min_ops = [0] * n
        
        for i in range(n):
            ops = 0
            for j in range(n):
                if boxes[j] == '1':
                    ops += abs(i - j)
            min_ops[i] = ops
        
        return min_ops
    