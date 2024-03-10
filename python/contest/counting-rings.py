"""
Bilbo is sitting in his chair, bored. In front of him sits Gandalf, who is leisurely smoking his pipe and amusing himself by shaping the smoke into various forms. Gandalf creates shapes represented by characters: a house denoted by "H", a ship denoted by "S", and a ring denoted by "O".

Bilbo is only interested in counting the consecutive rings Gandalf makes. He wants to know how many rings Gandalf creates in a row.

Given Gandalf's sequence of smoke shapes, help Bilbo determine the maximum number of consecutive rings Gandalf makes.

Input
The input consists of a single string 𝑠
 (1≤|𝑠|≤2∗105)
, where consists of characters 'H', 'S', and 'O', representing Gandalf's smoke shapes.

Output
Output a single integer, the maximum number of consecutive rings Gandalf makes.

Examples
inputCopy
HHHHOOSO
outputCopy
2
inputCopy
SSSSOOOHSHHHO
outputCopy
3
inputCopy
HHSS
outputCopy
0

"""


def count_rings():
    s = list(input())
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'O':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


print(count_rings())
