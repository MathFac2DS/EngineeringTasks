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

# Q2. given an integer n, return the number of trailing zeroes in n!.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # trailing zeros come from products with powers of 10: (2*5)^p
        # it suffices to show, find the number of factors of 5
        # test n = 625 => div = 625 > 0 => div = 125, fives_count = 125, repeat

        fives_count = 0
        dividend = n
        while dividend >= 5:
            dividend //= 5
            fives_count += dividend

        return fives_count

#Q3. given bounds left and right, find the pair of primes between left and right (inclusive) that are closest together. 
class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # two and three are the closest primes, when they are in the range
        if left <= 2 and 3 <= right: return [2, 3]

        # we need at least three elements to see a pair of primes, when two is not in the range
        if right - left < 3: return [-1, -1]

        # generate an array of natural numbers, starting with left and ending with right
        range_of_numbers = [k for k in range(left, right+1)]

        # generate a list of primes less than or equal to the int(sqrt(right))
        def get_primes(upper):
            # initialize the sieve
            is_prime = [True]*(upper + 1)
            is_prime[0] = is_prime[1] = False

            # separate primes and composites
            for p in range(2, int(sqrt(upper))+1):
                if is_prime[p] == True:
                    # mark all multiples of p as prime
                    for k in range(p*p, upper + 1, p): is_prime[k] = False

            # filter the list of numbers to include only the primes
            return [i for i, prime_flag in enumerate(is_prime) if prime_flag]

            # primes = []
            # for i, prime_flag in enumerate(is_prime):
            #     if prime_flag == True: primes.append(i)

        primes_in_range = [p for p in get_primes(right) if p >= left]
        
        # compute differences of consecutive primes in range
        differences = [primes_in_range[k+1] - primes_in_range[k] 
                        for k, _ in enumerate(primes_in_range) 
                        if k < len(primes_in_range) - 1]

        if not differences: return [-1, -1]
        min_diff = min(differences)
        idx = differences.index(min_diff)

        return [primes_in_range[idx], primes_in_range[idx + 1]]
