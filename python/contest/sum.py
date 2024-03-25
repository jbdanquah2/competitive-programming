t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    elements = list(map(int, input().split()))
    elements.sort()

    # print("k:", k)
    # print('elements:', elements)

    sum_smallest = sum(elements[:k])
    sum_largest = sum(elements[-k:])
    max_sum = max(sum_smallest, sum_largest)

    print(max_sum)
