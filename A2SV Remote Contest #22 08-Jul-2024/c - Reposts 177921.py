# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

def get_max_repost_chain_length():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    reposts = data[1:]
    
    repost_chain = {'polycarp': 1}  # Initial repost chain length with 'polycarp'

    for repost in reposts:
        name1, _, name2 = repost.lower().split()
        repost_chain[name1] = repost_chain[name2] + 1

    # The answer is the maximum value in repost_chain dictionary
    max_length = max(repost_chain.values())
    print(max_length)

get_max_repost_chain_length()
