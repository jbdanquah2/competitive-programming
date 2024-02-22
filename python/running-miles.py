def running_miles():
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        max_beauty = 0

        for i in range(1, n - 1):

            max_beauty = max(max_beauty, b[i - 1] + b[i] + b[i + 1] - 1)

        print(max_beauty)

running_miles()
