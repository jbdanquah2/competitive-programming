"""
Commander Master Cheifu is determined to win every battle with his team of 𝑛
 skilled soldiers, each possessing unique abilities. He seeks to determine the number of distinct arrangements for his soldiers, ensuring that each soldier defeats their parallel opponent from the opposing team. The opponent team also comprises 𝑛
 soldiers, and winning a battle is defined by each soldier prevailing over their specific opponent.

The number of arrangements must be computed modulo 109+7
 to accommodate the diverse ways the soldiers can be reordered for achieving success.

Two ways of arrangements are considered different if the resulting arrays are different.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤2⋅105
) — The number of soldiers in Master Cheifu's team (n) and the opposing team (n).

The second line of each test case contains 𝑛
 distinct integers 𝑎1
, 𝑎2
, …
, 𝑎𝑛
 (1≤𝑎𝑖≤109
) — representing the abilities of Master Cheifu's soldiers.. It is guaranteed that all elements are pairwise distinct.

The second line of each test case contains 𝑛
 integers 𝑏1
, 𝑏2
, …
, 𝑏𝑛
 (1≤𝑏𝑖≤109
) — representing the abilities of the opposing team.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output the count of unique arrangements for Master Cheifu's soldiers, considering the result modulo 109+7
.

Example
input:
5
6
9 6 8 4 5 2
4 1 5 6 3 1
3
4 3 2
3 4 9
1
2
1
3
2 3 4
1 3 3
12
2 3 7 10 23 28 29 50 69 135 420 1000
1 1 2 3 5 8 13 21 34 55 89 144
output:
32
0
1
0
13824
"""


MOD = 10**9 + 7

def count_unique_arrangements(n, a, b):
    a.sort()
    b.sort()
    ans = 1
    for i in range(n):
        diff = a[i] - b[i]
        if diff <= 0:
            return 0
        ans = (ans * diff) % MOD
    return ans

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        result = count_unique_arrangements(n, a, b)
        print(result)

if __name__ == "__main__":
    main()
