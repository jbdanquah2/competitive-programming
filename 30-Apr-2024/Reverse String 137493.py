# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str], left=0, right=None) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        # left, right = 0, len(s) - 1

        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        if right == None:
            right = len(s) - 1

        if left >= right:
            return None

        s[left], s[right] = s[right], s[left]

        self.reverseString(s, left+1, right-1)


        