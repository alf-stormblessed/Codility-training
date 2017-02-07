'''
Created on 6 feb. 2017

@author: accl
'''
import unittest
from codility.TapeEquilibrium.TapeEquilibrium import solution
import time
import matplotlib.pyplot as plt


class Test(unittest.TestCase):

    def testExample(self):

        A = [3, 1, 2, 4, 3]
        goal = 1
        assert goal == solution(A), "incorrect solution returned: " + str(solution(A)) \
            + " , instead of " + str(goal)

    def testlengthOf2(self):

        A = [3, 1]
        goal = 2
        assert goal == solution(A), "incorrect solution returned: " + str(solution(A)) \
            + " , instead of " + str(goal)

    def testLastTapeMinimal(self):

        A = [3, 1, 1, 5]
        goal = 0
        assert goal == solution(A), "incorrect solution returned: " + str(solution(A)) \
            + " , instead of " + str(goal)

    def testTimeComplexity(self):

        # N = 10
        A = [1] * 1000
        start1 = time.time()
        solution(A)
        end1 = time.time()
        dif1 = end1 - start1

        # N = 1000
        A = [1] * 10000
        start2 = time.time()
        solution(A)
        end2 = time.time()
        dif2 = end2 - start2

        # N = 100000
        A = [1] * 100000
        start3 = time.time()
        solution(A)
        end3 = time.time()
        dif3 = end3 - start3

        # N = 1000000
        A = [1] * 1000000
        start4 = time.time()
        solution(A)
        end4 = time.time()
        dif4 = end4 - start4

        plt.plot([1000, 10000, 100000, 1000000], [dif1, dif2, dif3, dif4])
        plt.ylabel('Time in seconds')
        plt.xlabel('Number of elements')
        plt.show()

if __name__ == "__main__":

    unittest.main()
