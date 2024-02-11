from collections import Counter

class Solution(object):

    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        winners = []
        loosers = []
        
        for match in matches:
            winners.append(match[0])
            loosers.append(match[1])

        winners_set = set(winners)
        loosers_set = set(loosers)

        win_list = list(winners_set - loosers_set)

        loosers_count = Counter(loosers)

        los_list = [num for num, count in loosers_count.items() if count == 1]

        return [sorted(win_list), sorted(los_list)]
        


        