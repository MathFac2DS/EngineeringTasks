## Q1. Can Make Arithmetic Progression From Sequence
    # A sequence of numbers is called an arithmetic progression if the difference between
    # any two consecutive elements is the same.
    # Given an array of numbers arr, return true if the array can be rearranged to form
    # an arithmetic progression. Otherwise, return false.

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # constraints include array length on [2,1000], and element size on [-10e6,10e6]
        # length = len(arr)
        # if 1 < length < 1001:
        #     print("passed length check")
        #     continue
        # else print("too long")

        # let's try that again with a while True wrap

        while True:
            try:
                length = len(arr)
                if 2 <= length <= 1000 and -10 ** 6 <= min(arr) and max(arr) <= 10 ** 6:
                    # reorder the list in ascending order
                    arr.sort()
                    differences = []
                    for i in range(1, length):
                        diff = arr[i] - arr[i - 1]
                        differences.append(diff)

                    if len(set(differences)) == 1:
                        return True
                    else:
                        return False
            except ValueError:
                print("Your array could not be understood.")

        # looks like the constraints are built in to Testcase in the platform;
        # not a list of requirements for me to meet

## Q2. Find the Pivot Integer
# Given a positive integer n, find the pivot integer x such that:

    # The sum of all elements between 1 and x inclusively equals
    # the sum of all elements between x and n inclusively.
    # Return the pivot integer x. If no such integer exists, return -1.
    # It is guaranteed that there will be at most one pivot index for the given input.

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        # built in constraints 1 <= n < 1000 ->  sum up to 1000, S = 1000*1001/2

        # let's try to brute force it first, then get clever
        # given an n, check every k from 1 to n for the equality Sum(1, k) = Sum(k, n)

        # from Gauss, define a function to calculate the sum of integers for a to b, inclusive
        def summation(a, b):
            sum_total = (b * (b + 1) + a * (1 - a)) / 2
            return sum_total

        sln = -1
        for k in range(1, n + 1):
            left_sum = summation(1, k)
            right_sum = summation(k, n)
            if left_sum == right_sum:
                sln = k
        if sln != -1: print(summation(1, sln), summation(sln, n))

        return sln

