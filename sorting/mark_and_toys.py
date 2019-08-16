import math
import os
import random
import re
import sys

def _mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr)//2

    left = _mergeSort(arr[:mid_idx])   
    right = _mergeSort(arr[mid_idx:])
    
    result = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    result += left[l:]
    result += right[r:]
    return result

def maximumToys(prices, k):
    maxToys = 0
    sorted_arr = _mergeSort(prices)
    for i in sorted_arr:
        if (k - i) > 0:
            k -= i
            maxToys += 1

    return maxToys


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
