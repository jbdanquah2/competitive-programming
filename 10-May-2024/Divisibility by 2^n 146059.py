# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

from functools import reduce

def make_product_divisible_by_2n(n, arr):
    total_product = reduce(lambda x, y: x * y, arr)

    if total_product % (2 ** n) == 0:
        return 0
    elif total_product == 0:
        return 1
    elif total_product % 2 == 1 or n == 1:
        return -1
    else:
        power_of_2 = 0
        while total_product % 2 == 0:
            power_of_2 += 1
            total_product //= 2
        
        operations_needed = n - power_of_2
        return operations_needed

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(make_product_divisible_by_2n(n, arr))
