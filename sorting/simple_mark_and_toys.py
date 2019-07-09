#!/bin/python3

import math
import os
import random
import re
import sys


def maximumToys(prices, k):

    maxToys = 0
    sorted_arr = sorted(prices)
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

