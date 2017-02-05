'''
Created on 4 feb. 2017

definition of the problem:
https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/

A: each element of A is an integer within the range -1000...1000
     N = len(A) is an integer within the range [0..100];

K: is an integer within the range [0..100];

@author: accl
'''


def solution(A, K):

    if K == 0:
        return A
    else:
        K = K % len(A)
        return A[-K:] + A[:-K]
