import itertools
from itertools import permutations, islice
import math

## Q1. Given n, k, find the kth permutation of the first n natural numbers

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # find in which of the n groups the kth element appears
        if k <= math.factorial(n-1): group = 1
        elif k % math.factorial(n-1) == 0: group = k / math.factorial(n - 1)
        else: group = int(k / math.factorial(n-1)) + 1
        position_in_group = k - (group - 1)*math.factorial(n - 1)

        # generate a list of the first n natural numbers
        list_natural = [i+1 for i in range(n)]
        permutes = islice(permutations(list_natural), (group-1)*math.factorial(n-1), group*math.factorial(n-1))
        list_permutes = []

        for p in permutes:
            string = ''.join(str(item) for item in p)
            list_permutes.append(string)


        return list_permutes[position_in_group-1]

## Q2. given numRows, print first numRows of Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # binomial expansion -> n_C_k in row n, column k for 1 <= k <= n
        # n_C_k = n! / (k!*(n-k)!)

        triangle = []
        n = numRows

        for j in range(0, n):
            current_row = [math.factorial(j) / (math.factorial(k)*math.factorial(j - k)) for k in range(0, j+1)]
            triangle.append(current_row)

        return triangle

## Q3. Find the number of ways to arrange n lengths such that k are left-visible
class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if k == 1: return math.factorial(n - 1) % (10**9 + 7)
        if k == n: return 1
        if k > n or k == 0: return 0
        stirling = [[1, 0]]
        # generate the first n rows of the stirling triangle, recursively
        for row in range(1, n+1):
            current_row = [0]
            for column in range(1, row+1):
                prev_row = stirling[row-1]
                above = (row-1)*(prev_row[column]) if column < len(prev_row) else 0
                corner = prev_row[column-1]
                stirling_number = above + corner
                current_row.append(stirling_number)
            current_row.append(0)
            stirling.append(current_row)
        return stirling[n][k] % (10**9 + 7)
