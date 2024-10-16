# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

def can_reach_cell(n, t, portals):
    current_position = 1  

    while current_position < t:
        current_position += portals[current_position - 1]  

    return "YES" if current_position == t else "NO"


n, t = map(int, input().split())
portals = list(map(int, input().split()))

result = can_reach_cell(n, t, portals)
print(result)
