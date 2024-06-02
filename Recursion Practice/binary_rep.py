import unittest


# Return binary representation of given integer
# 0 <= n <= 1000000
# Try to do it recursively.
# See test cases for examples
class BinaryRep:
    def __init__(self):
        pass

    def print_binary_rep(self, n):
        if n == 0:
            return ""
        return self.print_binary_rep(n//2) + str(n % 2)

    def print_binary_rep_iterative(self, n):

        if n == 0:
            return "0"
        result = ""
        while n > 0:
            result = str(n % 2) + result
            n = n // 2
        return result


class TestBinaryRep(unittest.TestCase):
    def test_solution(self):
        solution = BinaryRep()
        self.assertEqual(solution.print_binary_rep(3), "11")
        self.assertEqual(solution.print_binary_rep(42), "101010")
        self.assertEqual(solution.print_binary_rep(572), "1000111100")


if __name__ == "__main__":
    unittest.main()
