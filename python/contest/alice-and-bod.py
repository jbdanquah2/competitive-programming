def lexicographically_smallest_string(t):
    # Iterate through each test case
    for _ in range(t):
        n, m, k = map(int, input().split())
        alice = input().strip()
        bob = input().strip()

        # Sort Alice's string in ascending order
        alice_sorted = "".join(sorted(alice))

        # Sort Bob's string in descending order
        bob_sorted = "".join(sorted(bob, reverse=True))

        # Initialize the result string
        result = ""

        # Initialize pointers for Alice and Bob
        i, j = 0, 0

        # Alternate between Alice and Bob
        while i < n and j < m:
            # Select the smallest available character
            if alice_sorted[i] <= bob_sorted[j]:
                result += alice_sorted[i]
                i += 1
            else:
                result += bob_sorted[j]
                j += 1

        # Append remaining characters from Alice or Bob
        result += alice_sorted[i:] + bob_sorted[j:]

        print(result)

# Input
t = int(input())


# Solve and print the output
lexicographically_smallest_string(t)
