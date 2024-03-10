"""
Bilbo finds himself lost in a dark cave with only Gollum, whose real name is Smeagol, to assist him. However, Smeagol is willing to help under one condition: Bilbo must solve his riddle.

Smeagol will provide Bilbo with a set of words. Bilbo is allowed to change any letter in a word to any other letter in the alphabet as many times as he wants. For each word, Bilbo must determine the minimum number of letters he needs to change in order to transform the word into a palindrome. A palindrome is a word that reads the same forwards and backwards.

Input
The input consists of two lines:

The first line contains an integer 𝑛(1≤𝑛≤100)
, denoting the number of words provided by Smeagol. Following that, there are n lines, each containing a single word 𝑠𝑖
 (1≤|𝑠𝑖|≤2∗105)
 representing the words.

It is guaranteed that the sum of the lengths of the words does not exceed 2∗105
Each string consists of lowercase English letters only.

Output
Print 𝑛
 lines, each containing a single integer. The 𝑖
-th integer should represent the minimum number of letters Bilbo needs to change in order to turn the 𝑖
-th word into a palindrome.

Examples
inputCopy
1
ananas
outputCopy
3
inputCopy
2
racecar
gollum
outputCopy
0
2
Note
In the second example,

The string racecar is already a palindrome. Therefore we don't need to change any letters.

In the string gollum, after changing 'u' to 'o' and 'm' to 'g' the string becomes gollog, a palindrome.

"""


def is_palindrome(s):
    return s == s[::-1]


def smeagols_riddle():
    n = int(input())
    for _ in range(n):
        s = input()
        count = 0

        if is_palindrome(s):
            print(0)
            continue

        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                count += 1
        print(count)


smeagols_riddle()


