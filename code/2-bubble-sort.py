def BubbleSort(arr):
    arr_len = len(arr)

    for i in range(0, arr_len-1):
        for j in range(i+1, arr_len):
            if (arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr