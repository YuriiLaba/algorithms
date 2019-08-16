def _mergeSort(arr):
    if len(arr) == 1:
        return 0
    mid_idx = len(arr)//2

    left = arr[:mid_idx]   
    right = arr[mid_idx:]

    l_inversions = _mergeSort(left)
    r_inversions = _mergeSort(right)

    t_inversions = l_inversions + r_inversions
    
    l = 0
    r = 0
    counter = 0

    

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            arr[counter] = right[r]
            t_inversions += (len(left) - l)
            r += 1
            counter += 1
        else:
            arr[counter] = left[l]
            l += 1
            counter += 1

    while l < len(left):
        arr[counter] = left[l]
        counter += 1
        l += 1

    while r < len(right):
        arr[counter] = right[r]
        counter += 1
        r += 1

    return t_inversions

def countInversions(arr):
    n_swaps = _mergeSort(arr)
    print(n_swaps)

arr = [2, 1, 3, 1, 2]
countInversions(arr)