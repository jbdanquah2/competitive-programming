def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right  # returns the index of the largest element <= target

# Input processing
t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n_values = list(map(int, input().split()))
    
    # Sort the sequence a in ascending order
    a.sort()
    
    # Process each n_value
    for n in n_values:
        # Perform binary search to find the largest element <= n
        index = binary_search(a, n)
        winners = index + 1
        print(winners, end=' ')
    print()  # Move to the next line for the next test case

