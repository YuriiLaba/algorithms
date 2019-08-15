import math
import os
import random
import re
import sys


def _mergeSort(arr):
    if len(arr) != 1: 
        mid_idx = len(arr)//2 
        left_part = arr[:mid_idx]   
        right_part = arr[mid_idx:]
        _mergeSort(left_part) 
        _mergeSort(right_part)
        
        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]: 
                arr[k] = left_part[i] 
                i+=1
            else: 
                arr[k] = right_part[j] 
                j+=1
            k+=1

        while i < len(left_part): 
            arr[k] = left_part[i] 
            i+=1
            k+=1
          
        while j < len(right_part): 
            arr[k] = right_part[j] 
            j+=1
            k+=1
        return arr

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
