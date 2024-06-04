def determine_winner(t, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        plays = case[1]

        # Use a stack to simulate the game
        stack = []
        for play in plays:
            if stack and stack[-1] == play:
                stack.append(play)
            else:
                stack = [play]

        # Count the number of wins for each player
        wins_A = plays.count('A')
        wins_B = plays.count('B')

        # Determine the possible values of X and Y
        x_values = []
        y_values = []
        for i in range(1, n + 1):
            if n % i == 0:
                x_values.append(i)
                y_values.append(n // i)

        # Check each combination of X and Y
        winner_found = False
        for x in x_values:
            for y in y_values:
                if wins_A >= x and wins_B >= y and wins_A // x >= wins_B // y:
                    results.append('A')
                    winner_found = True
                    break
            if winner_found:
                break
        if not winner_found:
            results.append('B' if wins_B > wins_A else '?')

    return results

# Accept the number of test cases
t = int(input())

# Accept the test cases and store them in a list
test_cases = []
for _ in range(t):
    n = int(input())
    plays = input().strip()
    test_cases.append((n, plays))

# Determine the winner for each test case
output = determine_winner(t, test_cases)

# Print the results
for winner in output:
    print(winner)
