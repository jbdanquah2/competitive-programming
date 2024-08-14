# Problem: B - Firaols Contest - https://codeforces.com/gym/505936/problem/B



def main(n, arr: list):
    
    counter = [0] * n
    rounds_held = ""
    distinct_count = 0
    
    for i in range(m):
        difficulty = arr[i] - 1
        counter[difficulty] += 1
        
        if counter[difficulty] == 1:
            distinct_count += 1
        
        if distinct_count == n:
            rounds_held += "1"
            for j in range(n):
                counter[j] -= 1
                if counter[j] == 0:
                    distinct_count -= 1
        else:
            rounds_held += "0"
    
    print(rounds_held)
    
n, m = map(int, input().split())
arr = list(map(int, input().split()))
main(n, arr)
