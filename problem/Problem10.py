#!/usr/bin/python
# coding=utf-8
from Problem import Problem


class Problem10(Problem):
    """
    Summation of primes
    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    # FixMe not correct
    def solve(self):
        ret = []
        for number in range(1, 2000000):
            if Problem.is_prime(number):
                ret.append(number)
        print sum(ret)