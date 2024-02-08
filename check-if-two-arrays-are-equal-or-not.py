class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        a = sorted(A)
        b = sorted(B)

        
        return True if a == b else False