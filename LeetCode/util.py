import math
from math import sqrt

# given n returns k such that sum(1, k) = sum(k, n)
def pivotInteger(self, n):
    """
    :type n: int
    :rtype: int
    """

    # Gauss' sum from 1 to n
    sum_to_n = int(n * (n + 1) / 2)

    k = int(sqrt(sum_to_n))
    if k ** 2 == sum_to_n:
        return k
    else:
        return -1

# boolean check if given x is palindrome
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """

    digits_as_string = str(x)
    digits_reversed = digits_as_string[::-1]

    if digits_as_string == digits_reversed: return True
    else: return False

# Pascal's triangle generator
def generate_pascals(self, numRows):
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

# left visible: given n, k, generate the Stirling number (of the first kind)
def stirling_triangle(self, n, k):
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

# prime checker
def prime_check(k):
    upper_bound = int(sqrt(k))
    for j in range(2, upper_bound + 1):
        if k % j == 0: return False
    return True

def stirling_row(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if k > n or k == 0: return 0
    if k == n: return 1

    MOD = (10 ** 9 + 7)
    stirling_row = [0] * (k + 1)
    stirling_row[0] = 1

    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            stirling_row[j] = ((i - 1) * stirling_row[j] + stirling_row[j - 1]) % MOD
        # replace first element with 0, s(i, 0) = 0
        if i == 1: stirling_row[0] = 0

    return stirling_row[k]