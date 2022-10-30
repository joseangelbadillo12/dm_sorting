def quick_sort(array, low, high):
    if low < high:
    # Split and choose pivot
        pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)

def partition(array, low, high):  
# Pivot at the right
    pivot = array[high]

# Pointer of the smallest item
    i = low - 1

    for j in range(low, high):
        if float(array[j]['value']) <= float(pivot['value']):
        # Move pointer one position
            i = i + 1
        # Interchange elements
            (array[i], array[j]) = (array[j], array[i])

# At the end interchange the pivot
    (array[i + 1], array[high]) = (array[high], array[i + 1])

# Return the pivot at the original position
    return i + 1
