"""Demonstrate Merge Sort on an array of 15 floating-
point numbers and display the number of
comparisons made."""

# Global counter for comparisons
comparisons = 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    global comparisons
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge in sorted order
    while i < len(left) and j < len(right):
        comparisons += 1  # Increment counter for each comparison
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array, if any
    result.extend(left[i:])
    # Add remaining elements from right array, if any
    result.extend(right[j:])
    return result

# Example usage with an array of 15 floating-point numbers
if __name__ == "__main__":
    arr = [23.5, 12.8, 45.3, 9.1, 67.4, 33.2, 15.7, 88.6, 27.9, 51.3, 4.2, 76.5, 19.8, 62.1, 37.0]
    print("Original array:", arr)
    comparisons = 0  # Reset comparisons before sorting
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
    print("Number of comparisons:", comparisons)