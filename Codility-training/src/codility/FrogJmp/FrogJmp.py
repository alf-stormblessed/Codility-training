'''
Created on 5 feb. 2017

Definition of the problem
https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/

solution(X, Y, D)

X, Y, D: Integers in range 1..1,000,000,000
X <= Y

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).


@author: accl
'''


def solution(X, Y, D):

    if X == Y:
        return 0
    elif (Y-X) % D == 0:
        return (Y-X)//D
    else:
        return (Y-X)//D + 1
