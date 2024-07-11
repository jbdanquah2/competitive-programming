# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify the affected subtree
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        # Step 1: Build a max heap from the array
        self.buildHeap(arr, n)

        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            # Move current root to the end
            arr[i], arr[0] = arr[0], arr[i]

            # Call max heapify on the reduced heap
            self.heapify(arr, i, 0)