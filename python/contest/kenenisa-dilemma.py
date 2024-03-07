def find_swaps(num, my_list):

    check = []

    for i in range(num):
        min_index = i

        for j in range(i + 1, num):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            check.append((i, min_index))

    return check


n = int(input())
arr = list(map(int, input().split()))

swaps = find_swaps(n, arr)

print(len(swaps))

for swap in swaps:
    print(swap[0], swap[1])
