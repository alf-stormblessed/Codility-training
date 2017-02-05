'''
Created on 3 feb. 2017

@author: accl
'''
import unittest
from codility.OddOccurrencesInArray.OddOccurrencesInArray import solution


class Test(unittest.TestCase):

    def testExample(self):

        A = [9, 3, 9, 3, 9, 7, 9]
        assert solution(A) == 7, "solution returned: %r instead of 7" \
            % solution(A)

    def testUpperBoundary(self):
        A = [1000000000] * 999999
        A[0] = 999999999

        assert solution(A) == 999999999, \
            "solution returned: %r instead of 999999999" % solution(A)

    def testOneElementArray(self):

        A = [1]
        assert solution(A) == 1, "solution returned: %r instead of 1" \
            % solution(A)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
