class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_lst = s.split()
        s_lst.reverse()

        print(s_lst)

        return " ".join(s_lst)
    