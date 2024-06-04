
def mostFrequent(string: str):
    freq = {}

    for i in range(len(string)):
        curr = string[i]
        
        if curr in freq:
            freq[curr] += 1
        else:
            freq[curr] = 1

    return max(freq, key=freq.get)


t = int(input())

for _ in range(t):
    string = input()
    print(mostFrequent(string))