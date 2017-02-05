'''
Created on 5 feb. 2017

@author: accl
'''
import unittest
from codility.FrogJmp.FrogJmp import solution


class Test(unittest.TestCase):

    def testExample(self):

        X = 10
        Y = 85
        D = 30
        sol = solution(X, Y, D)
        goal = 3
        assert sol == goal, "incorrect solution: %(sol)r should have returned %(goal)r" \
            % {"sol": sol, "goal": goal}

    def testXEqualsY(self):

        X = 10
        Y = 10
        D = 1
        sol = solution(X, Y, D)
        goal = 0
        assert sol == goal, "incorrect solution: %(sol)r should have returned %(goal)r" \
            % {"sol": sol, "goal": goal}

    def testMaxXYD(self):

        X = 999999999
        Y = 1000000000
        D = 1000000000
        sol = solution(X, Y, D)
        goal = 1
        assert sol == goal, "incorrect solution: %(sol)r should have returned %(goal)r" \
            % {"sol": sol, "goal": goal}

if __name__ == "__main__":

    unittest.main()
