
# _*_ encoding: utf-8 _*_
"""Implement a radix sort."""
from __future__ import division
import time
from random import randint


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
    """Return avergae time of radix sort run."""
    for i in range(501):
        start = time.time()
        radix_sort(input_list)
        time_passed = time.time() - start
    avg_time = time_passed / 500
    return avg_time
