class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        lst = []

        for word in words:

            res1 = self.check_if_char_exist(word, "qwertyuiop")
            if res1 :
                lst.append(word)
                continue

            res2 = self.check_if_char_exist(word, "asdfghjkl")
            if res2:
                lst.append(word)
                continue

            res3 = self.check_if_char_exist(word, "zxcvbnm")
            if res3:
                lst.append(word)
                continue

        return lst

            
    
    def check_if_char_exist(self, word, keyboard_row):

        word_set = set(word.lower())

        for char in word_set:
            if char not in keyboard_row:
                return False
        
        return True

        