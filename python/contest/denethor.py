"""
In the kingdom of Gondor, King Denethor remains ever vigilant, overseeing the defense of the riverbanks against the looming threat of Mordor's forces. Denethor has a team of n commanders, each assigned a unique numerical identifier from 1
 to 𝑛
.

Denethor maintains a list of his commanders in that group, sorted by decreasing times of their last deployment to the riverbank. When a commander is deployed they are immediately moved to the front of the list (they will be first on the list), indicating their active duty. Importantly, only one commander is deployed at a time.

During one busy month, Denethor, preoccupied with state affairs, neglected to check the list until the first and last days of the month. Now, reflecting on his oversight, Denethor wonders about the minimum number of commanders who must have been deployed at least once between the first and last days of the month.

Denethor is sure that no two commanders are deployed at the same time and no commander was deployed when he checked the list on the first day of the month and on the last day of the month.

Input
Each test contains multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤10000
) — the number of test cases. The descriptions of the 𝑡
 test cases follow.

The first line of each test case contains an integer 𝑛
 (1≤𝑛≤105
) — the number of commanders Denethor has.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤𝑛
) — the list of unique numbers of the commanders, sorted by decreasing times of their last deployment at the start of the month.

The third line contains 𝑛
 integers 𝑏1,𝑏2,…,𝑏𝑛
 (1≤𝑏𝑖≤𝑛
) — the list of unique numbers of the commanders, sorted by decreasing times of their last deployment at the end of the month.

For all 1≤𝑖<𝑗≤𝑛
, it is guaranteed that 𝑎𝑖≠𝑎𝑗
 and 𝑏𝑖≠𝑏𝑗
.

It is also guaranteed that the sum of the values of 𝑛
 over all test cases does not exceed 105
.

Output
For each test case, print the minimum number of commanders that must have been deployed between the first and last days of the month.

Example
inputCopy
4
5
1 4 2 5 3
4 5 1 2 3
6
1 2 3 4 5 6
1 2 3 4 5 6
8
8 2 4 7 1 6 5 3
5 6 1 4 8 2 7 3
1
1
1
outputCopy
2
0
4
0
Note
In the first test case, commanders 4,5
 must have been deployed between the first and last days of the month

In the second test case, it is possible that nobody has been deployed between the first and last days of the month

"""


def minimum_number_of_commanders():

    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
