'''
Created on 4 feb. 2017

@author: accl
'''
import unittest
from codility.CyclicRotation.CyclicRotation import solution
from codility.utils.utils import formatList


class Test(unittest.TestCase):

    def testExample(self):

        A = [3, 8, 9, 7, 6]
        K = 3
        goal = [9, 7, 6, 3, 8]
        sol = solution(A, K)
        assert goal == sol, \
            "incorrect solution, should be " + formatList(goal) + \
            "instead of " + formatList(sol)

    def testZeroShift(self):

        A = [3, 8, 9, 7, 6]
        K = 0
        goal = A
        sol = solution(A, K)
        assert goal == sol, \
            "incorrect solution, should be " + formatList(goal) + \
            "instead of " + formatList(sol)

    def testOnePosShift(self):

        A = [3, 8, 9, 7, 6]
        K = 1
        goal = [6, 3, 8, 9, 7]
        sol = solution(A, K)
        assert goal == sol, \
            "incorrect solution, should be " + formatList(goal) + \
            "instead of " + formatList(sol)

    def testKBiggerThanLength(self):

        A = [3, 8, 9, 7, 6]
        K = 6
        goal = [6, 3, 8, 9, 7]
        sol = solution(A, K)
        assert goal == sol, \
            "incorrect solution, should be " + formatList(goal) + \
            "instead of " + formatList(sol)

if __name__ == "__main__":

    unittest.main()
