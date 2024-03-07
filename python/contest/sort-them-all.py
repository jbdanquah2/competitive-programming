def sort_problems(t, test_cases):
    for _ in range(t):
        n, a, b = test_cases[_]
        moves = []
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] > a[j] and b[i] > b[j]:
                    moves.append((i + 1, j + 1))
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]

        if sorted(a) == a and sorted(b) == b:
            print(len(moves))
            for move in moves:
                print(move[0], move[1])
        else:
            print(-1)


# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Solve and print output
sort_problems(t, test_cases)
