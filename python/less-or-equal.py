def find_x(num, k, sequence):
    sequence.sort()
    if k == 0:
        return sequence[0] - 1 if sequence[0] > 1 else -1
    elif k == num:
        return sequence[-1]
    elif sequence[k-1] == sequence[k]:
        return -1
    else:
        return sequence[k - 1]


n, k = map(int, input().split())
seq = list(map(int, input().split()))

x = find_x(n, k, seq)
print(x)
