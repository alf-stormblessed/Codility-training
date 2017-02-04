'''
Created on 3 feb. 2017

@author: accl

Problem explanation:
    https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

@var len(A):  is an odd integer within the range [1..1,000,000];

@var A: each element of array A is an integer
    within the range [1..1,000,000,000];
    all but one of the values in A occur an even number of times.

'''


def solution(A):

    total = 0

    for num in A:
        total ^= num

    return total
