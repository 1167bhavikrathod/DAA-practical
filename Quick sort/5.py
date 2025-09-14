"""Implement Quick Sort to arrange characters of a
string in alphabetical order."""
def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    print(pivot,end=" ")
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick(left) + [pivot] + quick(right)

string = "hellow world"
print("pivot elements :")
sorted = quick(string)
print("\nSorted:" , "".join(sorted))