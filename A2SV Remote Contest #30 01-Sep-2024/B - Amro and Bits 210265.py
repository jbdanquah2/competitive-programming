# Problem: B - Amro and Bits - https://codeforces.com/gym/545837/problem/B

def main(x):
    y = x & -x
    while True:
        if (x & y) > 0 and (x ^ y) > 0:
            return y
        y += 1

t = int(input())
for _ in range(t):
    x = int(input())
    print(main(x))
