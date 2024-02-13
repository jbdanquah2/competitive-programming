n = int(input())

responses_str = input()

responses = [int(num) for num in responses_str.split()]

if any(responses):
    print("HARD")
else:
    print("EASY")
