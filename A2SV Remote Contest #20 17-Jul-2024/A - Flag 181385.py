# Problem: A - Flag - https://codeforces.com/gym/531416/problem/A

def check_flag(n, m, flag):
    # Check each row to see if all columns are the same color
    for row in flag:
        if len(set(row)) != 1:
            return "NO"
    
    # Check adjacent rows to ensure they have different colors
    for i in range(n - 1):
        if flag[i][0] == flag[i + 1][0]:
            return "NO"
    
    return "YES"

# Read input
n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

print(check_flag(n, m, flag))
