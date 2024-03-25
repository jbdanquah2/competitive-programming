

def differing_indices(s1: str, s2: str):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]


t = int(input())
string = "codeforces"
count = 0
for _ in range(t):
    s = input()

    count = len(differing_indices(string, s))
    print(count)


