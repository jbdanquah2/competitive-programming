"""
For educational purposes, in the problems of this block, the time limit is large enough for the solution to pass in 𝑂(𝑛log𝑛)
 time, but try to write the solution in linear time, which we discussed in the lecture.

You are given two arrays, sorted in non-decreasing order. Merge them into one sorted array.

Input
The first line contains integers 𝑛
 and 𝑚
, the sizes of the arrays (1≤𝑛,𝑚≤105
). The second line contains 𝑛
 integers 𝑎𝑖
, elements of the first array, the third line contains 𝑚
 integers 𝑏𝑖
, elements of the second array (−109≤𝑎𝑖,𝑏𝑖≤109
).

Output
Print 𝑛+𝑚
 integers, the merged array.

Example
inputCopy
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
outputCopy
1 2 3 6 8 9 13 13 15 18 18 21 25
"""


def merge_arrays(n, m, a, b):
    result = []

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result + a[i:] + b[j:]


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = merge_arrays(n, m, a, b)
print(*res)

