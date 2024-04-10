def max_stones_display(N, S, stone_sizes):
    stone_sizes.sort()  # Sort the array of stone sizes
    left = 0
    maxStones = 0

    for right in range(N):
        while stone_sizes[right] - stone_sizes[left] > S:
            left += 1  # Move the left pointer if the difference exceeds S
        maxStones = max(maxStones, right - left + 1)  # Update maxStones

    return maxStones


# Input parsing
N, S = map(int, input().split())
stone_sizes = [int(input()) for _ in range(N)]

result = max_stones_display(N, S, stone_sizes)
print(result)
