# Problem: A - Divide Array - https://codeforces.com/gym/505936/problem/A


def main(arr: list, n: int):
    
    negative = []
    positive = []
    zero = []
    
    for i in range(n):
        if arr[i] < 0:
            negative.append(arr[i])
        elif arr[i] > 0:
            positive.append(arr[i])
        else:
            zero.append(arr[i])
            
    if len(positive) == 0:
        positive.append(negative.pop())
        positive.append(negative.pop())
        
    if len(negative) % 2 == 0:
        zero.append(negative.pop())

    print(len(negative), end=" ")
    print(*negative)
    print(len(positive), end=" ")
    print(*positive)
    print(len(zero), end=" ")
    print(*zero)
    
  
n = int(input())  
arr = list(map(int, input().split()))
main(arr, n)
