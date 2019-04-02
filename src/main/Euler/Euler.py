# coding: UTF-8

'''
Created on Mar 31, 2019

@see: https://projecteuler.net/
@author: hlubyluk
'''


def problem1():
    '''
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    return sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])


def problem2():
    '''
    Even Fibonacci numbers
    Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    '''
    fibonacci = [1, 2]
    while True:
        fibonacci_next = fibonacci[-2] + fibonacci[-1]
        if fibonacci_next >= 4000000:
            break
        fibonacci.append(fibonacci_next)
    return sum(filter(lambda item: item % 2 == 0, fibonacci))


def problem3():
    '''
    Largest prime factor

    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
    '''
    number, now = 600851475143, 2
    while number > 1:
        if number % now == 0:
            number /= now
        else:
            now += 1
    return now


def is_palindrome(items):
    return items == items[::-1]


def problem4():
    '''
    Largest palindrome product
    
    Problem 4
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.
    
    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    return sorted([a * b for a in range(100, 1001) for b in range(100, 1001)
                  if is_palindrome(str(a * b))])[-1]


def problem5():
    '''
    Smallest multiple

    Problem 5
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20?
    '''
    cache = dict()
    for x in range(2, 20 + 1):
        for k, v in prime_factorization(x).items():
            tmp = cache.get(k, 0)
            cache[k] = max(tmp, v)
    return reduce(mul, map(pow_tupple, cache.items()))


def prime_factorization(number):
    cache = dict()

    factor = 2
    x = number

    while x > 1:
        if x % factor == 0:
            tmp = cache.get(factor, 0)
            cache[factor] = tmp + 1
            x //= factor
        else:
            factor += 1

    return cache


def mul(a, b): return a * b


def pow_tupple(a): return a[0] ** a[1]


def problem6():
    '''
    Sum square difference

    Problem 6
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the
    first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of
    the first one hundred natural numbers and the square of the sum.
    '''
    r = range(1, 101)
    return pow_fun(sum(r), 2) - sum(map(lambda a: pow_fun(a, 2), r))


def pow_fun(a, b): return a ** b


def problem7():
    '''
    10001st prime

    Problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    '''
    count, i = 0, 1
    while True:
        count += (0, 1)[is_prime(i)]
        if count == 10001:
            return i
        i += 1

    return 0


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    tmp = 3
    while tmp * tmp <= n:
        if n % tmp == 0:
            return False

        tmp += 2

    return True


def problem8():
    '''
    Largest product in a series

    Problem 8
    The four adjacent digits in the 1000-digit number that
    have the greatest product are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that
    have the greatest product. What is the value of this product?
    '''
    number = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
    '''
    n = map(lambda a: ord(a) - ord('0'), list(number.replace("\n", "")))
    return max([reduce(mul, n[a:a + 13]) for a in range(len(n) - 13)])


if __name__ == '__main__':
    # print(problem1())
    # print(problem2())
    # print(problem3())
    # print(problem4())
    # print(problem5())
    # print(problem6())
    # print(problem7())
    # print(problem8())
    pass
