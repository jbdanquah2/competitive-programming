# Problem: A - FIA Heist - https://codeforces.com/gym/520098/problem/A

def decodeString():
    # Lewa<-isd<-
    s = input()
    stack = []
    i = 1
    while i < len(s)+1:
        c = s[i-1]
    
        if c == '<' and s[i] == '-':
            if stack:
                stack.pop()
            i += 1
        else:
            stack.append(c)
        i += 1

    return ''.join(stack)

print(decodeString())
