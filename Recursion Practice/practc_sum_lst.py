import unittest


# Return sum of the given list of numbers.
class SumList:
    def __init__(self):
        pass

    def sum_list(self, lst)->int:
        return self.recursive_sum(lst, 0)

    def recursive_sum(self, lst, index_num):
        if index_num+1 == len(lst):
            return 0
        # recursive_sum function finds the sum of the elements by summing up the lst[indx] and the rest of the lst
        return lst[index_num] + self.recursive_sum(lst, index_num+1)




class TestSumList(unittest.TestCase):
    def test_solution(self):
        solution = SumList()
        self.assertEqual(solution.sum_list([1, 2, 3, 4]), 10)
        self.assertEqual(solution.sum_list([10, 10, 10, 10]), 40)


if __name__ == '__main__':
    unittest.main()
