import math
import os
import random
import re
import sys
import time
import bisect


def _binarySearch(arr, el, left_idx, right_idx):
    mid = left_idx + int((right_idx - left_idx) // 2) - ((right_idx - left_idx) % 2 > 0)

    if left_idx == right_idx:
        return
    if arr[mid] == el:
        return mid
    elif arr[mid] < el:
        return _binarySearch(arr, el, mid, right_idx)
    elif arr[mid] > el: 
        return _binarySearch(arr, el, left_idx, mid)

def _binaryInsert(arr, el, left_idx, right_idx):
    mid = left_idx + int((right_idx - left_idx) / 2) - ((right_idx - left_idx) % 2 > 0)


    if left_idx == right_idx:
        return
    if  arr[mid-1] <= el <= arr[mid]:
        return mid
    elif arr[mid] < el:
        return _binaryInsert(arr, el, mid, right_idx)
    elif arr[mid] > el: 
        return _binaryInsert(arr, el, left_idx, mid)



def _getMedian(arr, median_idx):    
    if len(arr) % 2 == 0:
        median = (arr[median_idx] + arr[median_idx-1])/2
    else:
        median = arr[median_idx-1]
    return median    
    

def activityNotifications(expenditure, d):
        start_day = 0
        last_day = d
        num_notif = 0

        expenditure_portion = sorted(expenditure[start_day:last_day])
        median_idx = int(len(expenditure_portion) / 2) + (len(expenditure_portion) % 2 > 0)


        while last_day != len(expenditure)-1:
            median = _getMedian(expenditure_portion, median_idx)

            if expenditure[last_day] >= 2 * median:
                    num_notif += 1


            a = _binarySearch(expenditure_portion, expenditure[start_day], 0, len(expenditure_portion))
            del expenditure_portion[a]

            # bisect.insort(expenditure_portion, expenditure[last_day])
            if expenditure[last_day] >= expenditure_portion[-1]:
                expenditure_portion.insert(-1, expenditure[last_day])
            elif expenditure[last_day] <= expenditure_portion[0]:
                expenditure_portion.insert(0, expenditure[last_day])
            else:
                idx = _binaryInsert(expenditure_portion, expenditure[last_day], 0, len(expenditure_portion))
                expenditure_portion.insert(idx, expenditure[last_day])
            
            # expenditure_portion.append(expenditure[last_day])
            start_day += 1
            last_day += 1

        return num_notif

if __name__ == '__main__':

    d = 3

    with open("/home/laba/Project/hacker-rank/sorting/40001.txt") as f:
        lines = f.read().split(' ')
    # expenditure = list(map(int, lines))
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    # if(7 in sorted(expenditure)):
        # print("DDD")
    # d = _binarySearch(sorted(expenditure), 7, 0, len(expenditure))
    # print(d)
    # start = time.time()
    result = activityNotifications(expenditure, d)
    # end = time.time()

    # print(end - start)
    print(result)
    # lst = [ 2, 3, 6, 7, 8, 9, 10]
    # _binarySearch(lst, 10, 0, len(lst))
    # print(lst[a])


