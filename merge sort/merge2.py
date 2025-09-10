"""Implement Merge Sort to arrange names of
students in alphabetical order."""
def merge_sort(names):
    if len(names) <= 1:
        return names
    
    # Divide the list into two halves
    mid = len(names) // 2
    left = merge_sort(names[:mid])
    right = merge_sort(names[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare names from both lists and merge in alphabetical order
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():  # Case-insensitive comparison
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining names from left list, if any
    result.extend(left[i:])
    # Add remaining names from right list, if any
    result.extend(right[j:])
    return result

# Example usage with a list of 10 student names
if __name__ == "__main__":
    students = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Sophia", "Jackson", "Isabella", "Lucas", "Mia"]
    print("Original list of students:", students)
    sorted_students = merge_sort(students)
    print("Sorted list of students:", sorted_students)