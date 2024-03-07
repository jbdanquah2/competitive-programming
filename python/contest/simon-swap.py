from typing import List


def sort_string(arr: List[str]) -> None:

    size = len(arr)
    count = 0

    for j in range(size):
        for k in range(size - j - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                count += 1

    print(count)

    print("YES") if count <= 1 else print("NO")


t = int(input())

for i in range(t):
    my_arr = list(input())
    sort_string(my_arr)
