def count_divisible_pairs(N, M, spices):
    prefix_sums = [0]
    for s in spices:
        prefix_sums.append((prefix_sums[-1] + s) % M)

    remainder_freq = {}
    count = 0
    for i in range(N + 1):
        remainder = prefix_sums[i]
        count += remainder_freq.get(remainder, 0)
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

    return count

# Input processing
N, M = map(int, input().split())
spices = list(map(int, input().split()))

result = count_divisible_pairs(N, M, spices)
print(result)

