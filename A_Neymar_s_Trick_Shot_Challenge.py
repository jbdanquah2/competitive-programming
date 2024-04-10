n, x = map(int, input().split())
lengths = list(map(int, input().split()))

# Initialize variables
position = 0  # Starting position
bounces = 1  # Number of bounces within length X

# Simulate bounces
for length in lengths:
    position += length  # Update position after each bounce
    if position <= x:  # Check if ball is within length X
        bounces += 1  # Increment bounce count

# Output the result
print(bounces)