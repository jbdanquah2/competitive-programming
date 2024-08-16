# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # We use n+1 to handle out of bounds easily

        for i in range(n - 1, -1, -1):
            points = questions[i][0]
            brainpower = questions[i][1]
            next_index = i + brainpower + 1

            # Option 1: Solve the current question
            solve = points + (dp[next_index] if next_index < n else 0)

            # Option 2: Skip the current question
            skip = dp[i + 1]

            # Choose the best option
            dp[i] = max(solve, skip)

        return dp[0]
            