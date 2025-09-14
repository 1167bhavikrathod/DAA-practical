"""3. Demonstrate Quick Sort on a list of 20 random
numbers and display the pivot element at each
step."""

def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    print(pivot,end=" ")
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick(left) + [pivot] + quick(right)

nums = [5, 3, 8, 4, 2, 7, 1]
print("pivot elements :")
sorted = quick(nums)
print("\nSorted:" , sorted)