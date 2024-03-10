"""
In the cozy hobbit hole of Bag End, Frodo and Sam were engaged in a friendly game of number matching. Frodo had a list of 𝑛
 integers. Seeing Frodo's collection, Sam's competitive spirit ignited, and he resolved to create his own list.

To begin his quest, Sam scoured the Shire for a larger list of 𝑚
 integers (where 𝑚
 ≥ 𝑛
), His goal was to select 𝑛
 integers from the list and arrange them in a certain order to form his own list, aiming for a list as distinct as possible from Frodo's.

Specifically, Sam aimed to maximize the total difference 𝐷=∑𝑛𝑖=1|𝑎𝑖−𝑐𝑖|
 to be as large as possible. where 𝑎𝑖
 represented the integers in Frodo's list and 𝑐𝑖
 represented Sam's selected integers.

Assist Sam in his quest to uncover the maximum difference 𝐷
 he can achieve, ensuring his list stands out distinctly from Frodo's collection of digits.

Input
Each test consists of multiple test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤100
) — the number of test cases. This is followed by a description of the test cases.

The first line of each test case contains two integers 𝑛
 and 𝑚
 (1≤𝑛≤𝑚≤2⋅105
).

The second line of each test case contains 𝑛
 integers 𝑎𝑖
 (1≤𝑎𝑖≤109
). The third line of each test case contains 𝑚
 integers 𝑏𝑖
 (1≤𝑏𝑖≤109
).

It is guaranteed that in a test, the sum of 𝑚
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the maximum total difference 𝐷
 that Sam can obtain using his selected numbers.

Example
inputCopy
9
4 6
6 1 2 4
3 5 1 7 2 3
3 4
1 1 1
1 1 1 1
5 5
1 2 3 4 5
1 2 3 4 5
2 6
5 8
8 7 5 8 2 10
2 2
4 1
9 6
4 6
8 10 6 4
3 10 6 1 8 9
3 5
6 5 2
1 7 9 7 2
5 5
9 10 6 3 7
5 9 2 3 9
1 6
3
2 7 10 1 1 5
outputCopy
16
0
12
11
10
23
15
25
7
Note
In the first example, Sam can, for example, create the list (1,5,7,2)
. Then 𝐷=|6−1|+|1−5|+|2−7|+|4−2|=5+4+5+2=16
.

In the second example, all the integers are equal to 1, so Sam can only create the list (1,1,1)
, for which 𝐷=0
.

In the third example, Sam can, for example, create the list (5,4,3,2,1)
. Then 𝐷=|1−5|+|2−4|+|3−3|+|4−2|+|5−1|=4+2+0+2+4=12
.

"""

def maximum_difference():

    t = int(input())

