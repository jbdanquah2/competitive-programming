
n, s = map(int, input().split())
a = list(map(int, input().split()))

def segment_with_small_sum(n, s, a):

    curr_sum = 0
    left, right, = 0, 0
    main_count = 0

    for right in range(n):
        curr_sum += a[right]
        while curr_sum > s:
            curr_sum -= a[left]
            left += 1
        main_count = max(main_count, right - left + 1)

    print(main_count) 

segment_with_small_sum(n, s, a)