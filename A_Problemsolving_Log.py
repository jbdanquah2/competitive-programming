from collections import Counter

def number_of_solved_problems(n, log) -> int:
    probs_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    freq = Counter(log);
    count = 0

    for prob in freq:

        if freq[prob] >= probs_dict[prob] + 1:
            count += 1

    return count
        
    
t = int(input())

for _ in range(t):
    n = int(input())
    log = list(input())
    print(number_of_solved_problems(n, log))



