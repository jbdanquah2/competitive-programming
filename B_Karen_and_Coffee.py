n, k, q = map(int, input().split())
recipes = [tuple(map(int, input().split())) for _ in range(n)]
questions = [tuple(map(int, input().split())) for _ in range(q)]

# Create a list to store the count of admissible temperatures for each question
admissible_counts = []

# Iterate through each question
for a, b in questions:
    count = 0
    
    # Iterate through the range from a to b
    for temp in range(a, b + 1):
        temp_count = sum(1 for li, ri in recipes if li <= temp <= ri)
        
        # Check if the temperature is admissible
        if temp_count >= k:
            count += 1
    
    # Add the count to the list
    admissible_counts.append(count)

# Output the counts for each question
for count in admissible_counts:
    print(count)
