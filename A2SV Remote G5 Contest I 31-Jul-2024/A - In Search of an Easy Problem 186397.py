# Problem: A - In Search of an Easy Problem - https://codeforces.com/gym/500425/problem/A

n = int(input())

responses_str = input()

responses = [int(num) for num in responses_str.split()]

if any(responses):
    print("HARD")
else:
    print("EASY")
