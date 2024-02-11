class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        common = {}
        min_index = 0
        
        list1_dict = { list1[i]: i for i in range(len(list1))}
        list2_dict = { list2[i]: i for i in range(len(list2))}

        for key, value in list1_dict.items():
            if key in list2_dict.keys():
                common[key] = value + list2_dict[key]

        min_index = min([value for value in common.values() ])

        return [ key for key, value in common.items() if value == min_index ]
    