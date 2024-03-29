import math
import os
import random
import re
import sys


def countSwaps(a):
    numSwaps = 0

    # bubble sort approach
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                numSwaps += 1
                a[j], a[j+1] = a[j+1], a[j]

    return numSwaps


if __name__ == '__main__':
    n = int(input()) # number of elements in the input array
    a = list(map(int, input().rstrip().split())) # input array
    numSwaps = countSwaps(a)
    firstElement = a[0]
    lastElement = a[-1]
    print("Array is sorted in " + str(numSwaps) + " swaps.")
    print("First Element: " + str(firstElement))
    print("Last Element: " + str(lastElement))
