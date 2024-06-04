def min_moves_to_a_good(test_cases):
    for s in test_cases:
        moves = 0
        n = len(s)
        while n > 1:
            mid = n // 2
            first_half = s[:mid]
            second_half = s[mid:]

            if first_half == 'a' * mid:
                s = second_half
            elif second_half == 'a' * mid:
                s = first_half
            else:
                break
            n = len(s)

        for char in s:
            if char != 'a':
                moves += 1
        
        print(moves)

# Example usage:
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append(s)

min_moves_to_a_good(test_cases)
