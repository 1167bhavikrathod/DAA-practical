"""Write a program to implement Quick Sort on an
array of integers."""

def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick(left) + [pivot] + quick(right)

nums = [5, 3, 8, 4, 2, 7, 1]
print("Sorted:", quick(nums))