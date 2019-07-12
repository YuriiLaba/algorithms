import math
import os
import random
import re
import sys
import time
import bisect


def _binarySearch(arr, el, left_idx, right_idx):
    print(left_idx, right_idx)
    mid = left_idx + int((right_idx - left_idx) // 2)

    print(mid)
    # print(arr[mid])
    if arr[mid-1] == el:
        return mid
    elif arr[mid] > el:
        # print(arr[mid], el)
        return _binarySearch(arr, el, mid, right_idx)
    elif arr[mid] < el: 
        return _binarySearch(arr, el, left_idx, mid)
    
    # if right_idx >= left_idx: 
  
        # mid = int((right_idx - left_idx) / 2) + ((right_idx - left_idx) % 2 > 0)
        # print(mid)
        # If element is present at the middle itself 
        # if arr[mid] == el: 
            # return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        # elif arr[mid] > el: 
            # return _binarySearch(arr, el, left_idx, mid) 
  
        # Else the element can only be present  
        # in right subarray 
        # else: 
            # return _binarySearch(arr, el, mid, right_idx) 
  
    # else: 
        # Element is not present in the array 
        # return -1



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
            j = bisect.bisect_left(expenditure_portion, expenditure[start_day])
            print(a, j)
            del expenditure_portion[j]

            bisect.insort(expenditure_portion, expenditure[last_day])
            start_day += 1
            last_day += 1

        return num_notif


if __name__ == '__main__':

    d = 40001

    with open("/home/laba/Project/hacker-rank/sorting/40001.txt") as f:
        lines = f.read().split(' ')
    expenditure = list(map(int, lines))
    if(7 in sorted(expenditure)):
        print("DDD")
    _binarySearch(sorted(expenditure), 7, 0, len(expenditure))
    # start = time.time()
    # result = activityNotifications(expenditure, d)
    # end = time.time()

    # print(end - start)
    # print(result)
    # lst = [ 2, 3, 6, 7, 8, 9, 10]
    # _binarySearch(lst, 10, 0, len(lst))
    # print(lst[a])


