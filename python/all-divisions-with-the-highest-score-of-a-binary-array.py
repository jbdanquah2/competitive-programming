class Solution:
    def maxScoreIndices(self, nums):

        totalOnes = sum(nums)
        zerosToLeft = 0
        onesToRight = totalOnes

        scoreAtEachIndex = [totalOnes]

        for num in nums:

            if num == 0:
                zerosToLeft += 1
            else:
                onesToRight -= 1

            scoreAtEachIndex.append(zerosToLeft + onesToRight)

        maxScore = max(scoreAtEachIndex)

        maxIndices = [i for i, score in enumerate(scoreAtEachIndex) if score == maxScore]

        return maxIndices
