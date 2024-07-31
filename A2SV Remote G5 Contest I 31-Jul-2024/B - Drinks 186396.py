# Problem: B - Drinks - https://codeforces.com/gym/500425/problem/B

n = int(input())

vol_orange_juice_str = input()

vol_orange_juice = [int(num) for num in vol_orange_juice_str.split()]

sum_vol = sum(vol_orange_juice)

print(sum_vol/n)
