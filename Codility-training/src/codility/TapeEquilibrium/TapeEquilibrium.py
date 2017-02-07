# -*- coding: utf-8 -*-
'''
Created on 6 feb. 2017

@author: accl

Problem description:
https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

A:  each element of array A is an integer within the range −1000 to 1000
N = len(A) is an integer within the range 2 - 100000
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage
'''
import sys


def solution(A):

    total = sum(A)
    left_part = 0
    minimal_diff = sys.maxsize
    for index, number in enumerate(A):
        if (index == 0):
            left_part += number
        else:
            if (minimal_diff > abs(total - 2 * left_part)):
                minimal_diff = abs(total - 2 * left_part)
            left_part += number

    return minimal_diff
