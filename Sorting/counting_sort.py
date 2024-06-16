def countingsort(arr):
    max_val = max(arr)
    count = [0] * (max_val+1)

    while len(arr)>0:
        num = arr.pop(0)
        count[num]+=1
    
    for i in range(len(count)):
        while count[i]>0:
            arr.append(i)
            count[i]-=1
    
    return arr

unsortedArr = [8,3,3,0,4,2,1,1,6,5]
sortedArr = countingsort(unsortedArr)
print('Sorted VAr', sortedArr)