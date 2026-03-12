from math import sqrt

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

        arr.sort()

        difference = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != difference:
                return False
        return True



## Q2. Find the Pivot Integer

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Gauss' sum from 1 to n
        sum_to_n = int(n*(n+1)/2)

        k = int(sqrt(sum_to_n))
        if k**2 == sum_to_n: return k
        else: return -1

# Q3. Determine if the given integer is a palindrome
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        digits_as_string = str(x)
        digits_reversed = digits_as_string[::-1]

        if digits_as_string == digits_reversed: return True
        else: return False