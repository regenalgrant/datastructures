# _*_ encoding: utf-8 _*_
"""Implement a radix sort."""
from __future__ import division
import time
from random import randint


def quick_sort(alist):
    """Implement a quick sort on a list."""
    low = []
    high = []
    # import pdb; pdb.set_trace()
    try:
        pivot = alist[0]
        for i in alist[1:]:
            if isinstance(i, str):
                raise TypeError("List can not contain string.")
            high.append(i) if i > pivot else low.append(i)
        return quick_sort(low) + [pivot] + quick_sort(high)
    except IndexError:
        return []


def radix_sort(alist):
    """Implementation of radix."""
    if not alist:
        return alist
    tens = 10
    for i in range(len(str(max(alist)))):
        bucket = [[] for x in range(10)]
        for num in alist:
            bucket[(num % tens) // (tens // 10)].append(num)
        tens *= 10
        alist = [num for li in bucket for num in li]
    return alist

def time_it(input_list):
    """Average time of radix sort."""
    for i in range(501):
        start = time.time()
        radix_sort(input_list)
        time_passed = time.time() - start
    avg_time = time_passed / 500
    return avg_time

if __name__ == '__main__':
    small_list = time_it([2, 1])
    large_list = time_it([randint(0, 1000000) for i in range(10000)])
    print("Radix sorts a list ones, tens, hundreds, values and placing in containers"
        "or, buckets. Then merge all back together.")
    print("Input: [2, 1]\n\tnumber of runs: 500\n\taverage time: {}".format(small_list))
    print("Input: [randint(0, 1000000) for i in range(10000)]\n\tnumber of runs: 500\n\taverage time: {}".format(large_list))
