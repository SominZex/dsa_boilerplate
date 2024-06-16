def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [2,7,21,1,67,23,65,10,12,34,5,34]
targetVal = 10

result = linearSearch(arr, targetVal)

if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")