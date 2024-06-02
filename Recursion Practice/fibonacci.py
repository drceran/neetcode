import unittest


class Fibonacci:
    def __init__(self):
        pass

    def new_problem(self):
        ## Write a function that returns fibonacci of 5.
        self.get_fibonacci(5)


    def get_fibonacci(self, n):
        # Remove pass and write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.get_fibonacci(n-1) + self.get_fibonacci(n-2)


class TestFibonacci(unittest.TestCase):
    def test_solution(self):
        solution = Fibonacci()
        self.assertEqual(solution.get_fibonacci(9), 34)
        self.assertEqual(solution.get_fibonacci(5), 5)


if __name__ == '__main__':
    unittest.main()
