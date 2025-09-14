"""Implement Quick Sort to sort student marks in
descending order."""


def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick(right) + [pivot] + quick(left)

marks = [5, 3, 8, 4, 2, 7, 1]
print("Sorted:", quick(marks))