def MaximumElement(arr):
    i = 0
    maximum = arr[i]
    arr_len = len(arr)

    while (i < arr_len):
        if (maximum < arr[i]):
            maximum = arr[i]
            
        i = i + 1

    return maximum
