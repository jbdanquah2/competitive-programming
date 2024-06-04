def can_sort_by_swaps(n, a):
    even_numbers = [x for x in a if x % 2 == 0]
    odd_numbers = [x for x in a if x % 2 != 0]
    
    sorted_even = sorted(even_numbers)
    sorted_odd = sorted(odd_numbers)
    
    even_idx = 0
    odd_idx = 0
    
    sorted_combined = []
    for num in a:
        if num % 2 == 0:
            sorted_combined.append(sorted_even[even_idx])
            even_idx += 1
        else:
            sorted_combined.append(sorted_odd[odd_idx])
            odd_idx += 1
    
    return sorted_combined == sorted(a)


t = int(input())
results = []

for _ in range(t):
    
    n = int(input())
    data = list(map(int, input().split()))

    if can_sort_by_swaps(n, data):
        results.append("YES")
    else:
        results.append("NO")

# Output results
for result in results:
    print(result)
