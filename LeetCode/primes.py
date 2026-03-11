# Q1. count the primes
# given an integer n, return the number of prime numbers that are strictly less than n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # # check natural numbers less than sqrt(k) to see if they divide k
        # def prime_check(k):
        #     upper_bound = int(sqrt(k))
        #     for j in range(2, upper_bound + 1):
        #         if k % j == 0: return False
        #     return True

        if n < 3: return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        upper_bound = int(sqrt(n))

        for i in range(2, upper_bound + 1):
            if is_prime[i]:
                is_prime[i ** 2:n:i] = [False] * len(range(i ** 2, n, i))
        return sum(is_prime)