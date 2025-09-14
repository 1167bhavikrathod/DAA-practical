"""Apply Quick Sort to sort product prices and
display the sorted list."""

def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if arr[1] <= pivot]
    right = [i for i in arr[1:] if arr[1] > pivot]
    return quick(left) + [pivot] + quick(right)


products = [
    ("15 pro max",150000),
    ("14 pro max",140000),
    ("13 pro max",130000),
    ("12 pro max",120000),
    ("11 pro max",110000)
]
sorted = quick(products)
for product,price in sorted:
    print(f"{product}:{price}")

