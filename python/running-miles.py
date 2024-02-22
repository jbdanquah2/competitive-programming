"""
There is a street with 𝑛
 sights, with sight number 𝑖
 being 𝑖
 miles from the beginning of the street. Sight number 𝑖
 has beauty 𝑏𝑖
. You want to start your morning jog 𝑙
 miles and end it 𝑟
 miles from the beginning of the street. By the time you run, you will see sights you run by (including sights at 𝑙
 and 𝑟
 miles from the start). You are interested in the 3
 most beautiful sights along your jog, but every mile you run, you get more and more tired.

So choose 𝑙
 and 𝑟
, such that there are at least 3
 sights you run by, and the sum of beauties of the 3
 most beautiful sights minus the distance in miles you have to run is maximized. More formally, choose 𝑙
 and 𝑟
, such that 𝑏𝑖1+𝑏𝑖2+𝑏𝑖3−(𝑟−𝑙)
 is maximum possible, where 𝑖1,𝑖2,𝑖3
 are the indices of the three maximum elements in range [𝑙,𝑟]
.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤105
) — the number of test cases.

The first line of each test case contains a single integer 𝑛
 (3≤𝑛≤105
).

The second line of each test case contains 𝑛
 integers 𝑏𝑖
 (1≤𝑏𝑖≤108
) — beauties of sights 𝑖
 miles from the beginning of the street.

It's guaranteed that the sum of all 𝑛
 does not exceed 105
.

Output
For each test case output a single integer equal to the maximum value 𝑏𝑖1+𝑏𝑖2+𝑏𝑖3−(𝑟−𝑙)
 for some running range [𝑙,𝑟]
.

Example:
4
5
5 1 4 2 3
4
1 1 1 1
6
9 8 7 6 5 4
7
100000000 1 100000000 1 100000000 1 100000000
Output:
8
1
22
299999996

Note
In the first example, we can choose 𝑙
 and 𝑟
 to be 1
 and 5
. So we visit all the sights and the three sights with the maximum beauty are the sights with indices 1
, 3
, and 5
 with beauties 5
, 4
, and 3
, respectively. So the total value is 5+4+3−(5−1)=8
.

In the second example, the range [𝑙,𝑟]
 can be [1,3]
 or [2,4]
, the total value is 1+1+1−(3−1)=1
.
"""

# // solve the problem in python making sure to use a hashmap or a dict and it passes the test case above and any other test cases you can think of:
def running_miles():
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        max_beauty = 0

        for i in range(1, n - 1):

            max_beauty = max(max_beauty, b[i - 1] + b[i] + b[i + 1] - 1)

        print(max_beauty)

running_miles()
