# Problem: B - Chat room - https://codeforces.com/gym/540348/problem/B

def check_hello(s):
    target = "hello"
    target_index = 0
    
    for char in s:
        if char == target[target_index]:
            target_index += 1
            if target_index == len(target):
                return "YES"
    return "NO"

# Reading input
s = input().strip()
print(check_hello(s))
