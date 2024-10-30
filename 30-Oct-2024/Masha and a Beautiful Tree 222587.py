# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def min_swaps_to_beautiful_tree(m, p):
    def helper(subtree):
        # Base case: single node (leaf)
        if len(subtree) == 1:
            return 0, subtree

        # Split subtree into left and right halves
        half = len(subtree) // 2
        left, right = subtree[:half], subtree[half:]

        # Recursive count for left and right halves
        left_swaps, sorted_left = helper(left)
        right_swaps, sorted_right = helper(right)

        # If either side was impossible to sort, return -1
        if left_swaps == -1 or right_swaps == -1:
            return -1, []

        # Check if current left is less than right, otherwise swap
        if sorted_left[-1] < sorted_right[0]:
            # No swap needed
            return left_swaps + right_swaps, sorted_left + sorted_right
        elif sorted_right[-1] < sorted_left[0]:
            # One swap needed
            return left_swaps + right_swaps + 1, sorted_right + sorted_left
        else:
            # Cannot make this subtree beautiful
            return -1, []

    # Start recursion on the full list
    result, sorted_tree = helper(p)
    return result

# Input reading and processing
t = int(input())
results = []
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    results.append(min_swaps_to_beautiful_tree(m, p))

# Output results
print("\n".join(map(str, results)))
