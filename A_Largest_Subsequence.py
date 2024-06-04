def min_operations(t, test_cases):
    result = []
    for case in test_cases:
        n = case[0]
        s = case[1]
        max_char = s[0]
        max_pos = 0
        for i in range(1, n):
            if s[i] >= max_char:
                max_char = s[i]
                max_pos = i
        if s == ''.join(sorted(s)):
            result.append(0)
        elif s[max_pos:] + s[:max_pos] == ''.join(sorted(s)):
            result.append(1)
        else:
            result.append(-1)
    return result

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

output = min_operations(t, test_cases)
for ans in output:
    print(ans)
