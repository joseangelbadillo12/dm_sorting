def bubbleSort(arr):
    size = len(arr)
    swapped = False
    for i in range(size):
        min_index = i
        for j in range(i - 1, size):
            if arr[j]["value"] > arr[j]["value"]:
                swapped = True
                arr[j], arr[min_index] = arr[min_index], arr[j]
        
        if not swapped:
            return