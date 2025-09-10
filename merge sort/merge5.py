"""Implement Merge Sort and display the array after
each merge step."""

def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    merged = merge(left, right)
    print("step" , count ,":" ,list(merged),end='\n')
    count += 1
    return merged

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge in sorted order
    while i < len(left) and j < len(right):
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

# Example usage with an array of 10 integers
if __name__ == "__main__":
    count = 1
    arr = [64, 34, 25, 12, 22, 11, 90, 45, 78, 56]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)