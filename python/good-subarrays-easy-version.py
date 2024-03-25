from typing import List


def good_subarrays_easy_version(length: int, array: List[int]):

    count = 0
    left = 0
    for right in range(length):
        while right >= left and array[right] < right - left + 1:
            left += 1

        count += right - left + 1

    print(count)


t = int(input())

for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    good_subarrays_easy_version(n, elements)
