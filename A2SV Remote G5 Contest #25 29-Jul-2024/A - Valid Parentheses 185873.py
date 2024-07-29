# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

def main(s: str) -> int:
    
    result = 0
    open_brackets = 0
    
    for i in s:
        if i == '(':
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
                result += 2
                
    return result

s = input()
print(main(s))
