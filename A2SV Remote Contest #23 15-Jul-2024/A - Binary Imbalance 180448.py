# Problem: A - Binary Imbalance - https://codeforces.com/gym/535309/problem/A

def main(t, test_cases):
    results = []
    
    for case in test_cases:
        n, s = case
        count_0 = s.count('0')
        count_1 = s.count('1')
        
        if count_0 > count_1:
            results.append("YES")
        else:
            can_insert_zero = False
            for i in range(n - 1):
                if s[i] != s[i + 1]:
                    can_insert_zero = True
                    break
            
            if can_insert_zero:
                results.append("YES")
            else:
                results.append("NO")
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

results = main(t, test_cases)

for result in results:
    print(result)

