# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # if rowIndex == 0:
        #     return [1]

        # pre_row = [1]
        # for i in range(1, rowIndex + 1):
        #     curr_row = [1]
        #     for j in range(1, i):
          
        #         if len(pre_row) >= 2:
        #             curr_row.append(pre_row[j - 1] + pre_row[j])
               
        #     curr_row.append(1)
        #     pre_row = curr_row

        # return pre_row

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            curr_row = [1]

            for i in range(1, rowIndex):
                if len(prev_row) >= 2:
                    curr_row.append(prev_row[i - 1] + prev_row[i])
            curr_row.append(1)
            return curr_row


            

