# Problem: A - To My Critics - https://codeforces.com/gym/524150/problem/A


def main(nums):

    left, right = 0, 2


    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] + nums[mid - 1] >= 10:
            return 'YES'
        elif nums[mid] + nums[mid + 1] >= 10:
            return 'YES'
        elif nums[mid - 1] + nums[mid + 1] >= 10:
            return 'YES'
        else:
            return 'NO'
        
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    print(main(nums))
