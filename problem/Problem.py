from abc import abstractmethod


class Problem(object):
    """
    Abstract parent class
    Must implement method solve
    """

    NOT_IMPLEMENTED = "Not implemented!!!"

    @abstractmethod
    def solve(self):
        """
        Implementation of solution of problem.
        print result.
        """
        raise NotImplementedError('subclasses must override solve() method!')

    @staticmethod
    def is_prime(number):
        """
        Try prime factorization
        :param number: int to resolve
        :return: if is prime number return True, otherwise False
        """
        if number == 2:
            return True
        if number % 2 == 0 or number < 2:
            return False
        for i in range(3, int(number ** .5) + 1, 2):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def triangle_number(number):
        """
        This sequence is generated from a pattern of dots which form a triangle.
        By adding another row of dots and counting all the dots we can find the next number of the sequence.
        :param number: edge of triangle
        :return: count of triangles.
        """
        return (number * (number + 1)) / 2

    @staticmethod
    def count_dividers(number):
        """
        Compute count of dividers.
        :param number: to factorization.
        :return: count of dividers.
        """
        ret = 0
        for i in range(1, int(number ** .5)):
            if number % i == 0:
                ret += 1
        return ret * 2

    def binomical_coeficient(self, n, k):
        """
        Compute combination number. k is lower or equal n. https://en.wikipedia.org/wiki/Combination
        :param n: count of set.
        :param k: count of sub-set.
        :return: count of combinations.
        """
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def factorial(self, n):
        """
        Factorial of number.
        :param n: number.
        :return: multiplication of all number from n to 1.
        """
        if n == 1:
            ret = 1
        else:
            ret = n * self.factorial(n - 1)
        return ret

    def is_amicable(self, a):
        """
        Check sum of dividers number is same like sum of dividers
        of his sum of dividers.
        :param a: number
        :return: True if is amicable, otherwise False.
        """
        b = self.sum_of_dividers(a)
        return a == self.sum_of_dividers(b) and a != b

    def sum_of_dividers(self, a):
        """

        :param a:
        :return:
        """
        return sum([i for i in range(1, int((a / 2) + 1)) if a % i == 0])

    def prime_dividers(self, a):
        i, j, tmp = a, 2, []
        if self.is_prime(a):
            tmp.append(a)
        else:
            while i > 0 and i >= j:
                if i % j == 0:
                    tmp.append(j)
                    i /= j
                else:
                    j += 1
        return list(tmp)


    def is_perfect_number(self, i):
        return self.sum_of_dividers(i) == i

    def is_abundant_number(self, i):
        return self.sum_of_dividers(i) > i

    def nextLexicographicPermutations(self, sequence):
        i, j = len(sequence) - 2, len(sequence) - 1

        while i > 0 and sequence[i] >= sequence[i + 1]:
            i -= 1
            
        if (i <= 0):
            return False

        while j > 0 and sequence[j] <= sequence[i]:
            j -= 1

        tmp = sequence[i]
        sequence[i] = sequence[j]
        sequence[j] = tmp

        x, y = i + 1, len(sequence) - 1
        clone = list(sequence)
        while x < y:
            sequence[x] = clone[y]
            sequence[y] = clone[x]

            x += 1
            y -= 1
        
        return True
    
    
    def next_permutation(self, arr):
        # Find non-increasing suffix
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        if i <= 0:
            return False
        
        # Find successor to pivot
        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        arr[i - 1], arr[j] = arr[j], arr[i - 1]
        
        # Reverse suffix
        arr[i : ] = arr[len(arr) - 1 : i - 1 :-1]
        return True


    def gcd(self, a, b):
        """
        Great common divider.
        """
        x, y = 0, 0
        if a > b:
            x = a
            y = b
        else:
            x = b
            y = a
        while x % y != 0:
            tmp = x
            x = y
            y = tmp % x
        return y

    def fib(self, x):
        """
        X number in fibonacci sequence.
        """
        counter, a, b = 0, 0, 1
        while counter < x:
            a, b = b, a + b
            counter += 1
        return b


    def is_palindrome_10(self, a):
        x = str(a)
        return x[::1] == x[::-1]


    def is_palindrome_2(self, a):
        x = bin(a)[2::]
        return x[::1] == x[::-1]


    def pandigital_number(self, a):
        return cmp(list("123456789"), sorted(list(a))) == 0
        pass
