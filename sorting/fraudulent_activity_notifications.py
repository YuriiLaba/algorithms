#!/bin/python3

import math
import os
import random
import re
import sys
import time

def _customnSort(arr, new_el):
    del arr[0]
    # arr.append(new_el)
    # arr.sort()
    for i in range(len(arr)):
        if arr[i] >= new_el:
            arr.insert(i, new_el)
            return
    arr.insert(-1, new_el)
    # return arr

def activityNotifications(expenditure, d):

    num_notif = 0
    sub_len = d

    expenditure_ = sorted(expenditure[0:d])

    med_idx = int(d / 2) + (d % 2 > 0)


    while d != len(expenditure)-1:
        
        # print(expenditure_)
        # if sub_len % 2 == 0:
        #     med = (expenditure_[med_idx] + expenditure_[med_idx-1])/2
        # else:
        #     med = expenditure_[med_idx-1]

        import statistics

        med = statistics.median(expenditure_)

        # print(expenditure[d], 2 * med)
        if expenditure[d] >= 2 * med:
            num_notif += 1

        
        d += 1
        # print(d)
        expenditure_ = _customnSort(expenditure_, expenditure[d])

    return num_notif


if __name__ == '__main__':

    d = 3000

    with open("/home/laba/Project/hacker-rank/sorting/arr.txt") as f:
        lines = f.read().split(' ')
    expenditure = list(map(int, lines))
    # print(expenditure[:10])

    result = activityNotifications(expenditure, d)
    print(result)
