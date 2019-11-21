def elimination(arr):
    twins = None
    for index, num in enumerate(arr):
        if num in arr[index+1:]:
            twins = num
    return twins