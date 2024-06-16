def partition(array, low, high):
    pivot = array[high]
    i = low-1

    for j in range(low, high):
        if array[j]<=pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array)-1

    if low<high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [56,9,12,54,23,11,26,32,48]
quicksort(my_array)
print('Sorted', my_array)