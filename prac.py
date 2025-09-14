def mergesort(arr):
    global count
    if len(arr)<=1:
        return arr
    
    #divide array into two sub arrays
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    merged_array = merge(left,right)
    print("step" , count , ":",list(merged_array),end='\n')
    count+=1
    return merged_array



def merge(left,right):
    result = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    count = 1
    arr = [0,9,8,7,6,5,4,3,2,1]
    print("original array:",arr,end = '\n')
    sorted = mergesort(arr)
    print("sorted array:",sorted)
