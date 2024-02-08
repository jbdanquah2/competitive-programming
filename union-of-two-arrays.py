class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        all_list = list(set(a + b))
        
        return len(all_list)
    