def sort(n, arr):
    if n == 1:
        return arr
    
    arr = sort(n-1, arr)
    arr[n-1], arr[n-2] = arr[n-2], arr[n-1]

    return arr

def generate_permutation(n):
    arr = list(range(1, n+1))  # Create a list from 1 to n
    sorted_arr = sort(n, arr)  # Apply the sorting function
    return ' '.join(map(str, sorted_arr))  # Convert integers to strings and join them with spaces

# Example usage:
n = int(input())
permutation = generate_permutation(n)
print(permutation)
