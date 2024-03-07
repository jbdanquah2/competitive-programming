"""
You are given two arrays, sorted in non-decreasing order. For each element of the second array, find the number of elements in the first array strictly less than it.

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
Print 𝑚
 numbers, the number of elements of the first array less than each of the elements of the second array.

Example
inputCopy
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
outputCopy
1 1 2 3 4 6 6

"""

def number_of_smaller(n, m, a, b):

    result = []

    for i in range(m):
        count = 0
        for j in range(n):
            if a[j] < b[i]:
                count += 1
        result.append(count)
    return result


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


res = number_of_smaller(n, m, a, b)

print(*res)