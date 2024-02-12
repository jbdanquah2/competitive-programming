class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest = max(candies)

        result = []

        for num in candies:
            if num + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result
    