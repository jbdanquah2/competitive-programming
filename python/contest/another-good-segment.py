def count_good_segments(n, s, arr):
    left, right = 0, 0
    count = 0
    freq = {}
    distinct_count = 0

    while right < n:
        if arr[right] not in freq or freq[arr[right]] == 0:
            distinct_count += 1
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while distinct_count > s:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1
            left += 1

        count += right - left + 1
        right += 1

    return count

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(count_good_segments(n, s, arr))

