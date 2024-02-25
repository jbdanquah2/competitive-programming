class Solution:
    def maxScoreIndices(self, nums):

        total_ones = sum(nums)
        zeros_to_left = 0
        ones_to_right = total_ones

        score_at_each_index = [total_ones]

        for num in nums:

            if num == 0:
                zeros_to_left += 1
            else:
                ones_to_right -= 1

            score_at_each_index.append(zeros_to_left + ones_to_right)

        max_score = max(score_at_each_index)

        max_indices = [i for i, score in enumerate(score_at_each_index) if score == max_score]

        return max_indices
