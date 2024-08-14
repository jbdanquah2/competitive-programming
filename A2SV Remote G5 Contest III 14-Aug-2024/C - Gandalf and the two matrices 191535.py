# Problem: C - Gandalf and the two matrices - https://codeforces.com/gym/505936/problem/C

def solve():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    
    operations = []
    
    # Create a matrix B initialized with 0s
    B = [[0] * m for _ in range(n)]
    
    # Iterate through the matrix and find 2x2 blocks of 1s
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and A[i + 1][j] == 1 and A[i + 1][j + 1] == 1:

                operations.append((i + 1, j + 1))
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
    
    if A == B:
        print(len(operations))
        for op in operations:
            print(op[0], op[1])
    else:
        print(-1)

solve()

