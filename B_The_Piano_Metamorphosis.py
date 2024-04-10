def find_min_planks(n, k, heights):
    min_sum = float('inf')
    min_index = -1
    curr_sum = sum(heights[:k])  # Sum of first k planks
    
    for i in range(n - k + 1):
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_index = i
        
        # Slide the window
        if i + k < n:
            curr_sum = curr_sum - heights[i] + heights[i + k]
    
    return min_index + 1  # Adjust for 1-based indexing


n, k = map(int, input().split())
heights = list(map(int, input().split()))

result = find_min_planks(n, k, heights)
print(result)
