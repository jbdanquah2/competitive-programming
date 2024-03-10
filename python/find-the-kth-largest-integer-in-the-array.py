from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_arr = [int(n) for n in nums]
        nums_arr = sorted(nums_arr, reverse=True)

        kth_largest = nums_arr[k - 1]

        return str(kth_largest)