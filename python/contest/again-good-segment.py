from collections import Counter


def count_good_segments(n, k, arr):
    good_segments = 0
    count = Counter()
    mode_freq = 0
    left = 0

    for right in range(n):
        count[arr[right]] += 1
        mode_freq = max(mode_freq, count[arr[right]])

        while right - left + 1 > mode_freq * k:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1

        if mode_freq >= k:
            good_segments += 1

    return good_segments


n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = count_good_segments(n, k, arr)
print(result)
