import unittest
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_value = max(nums)
        counts_list = (max_value + 1) * [0]

        for num in nums:
            counts_list[num] += 1

        i = 0
        for num in range(len(counts_list)):
            for _ in range(counts_list[num]):
                nums[i] = num
                i += 1

class TestSortColors(unittest.TestCase):
    def test_sort_colors(self):
        solution = Solution()
        test_cases = [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),
            ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
            ([1, 2, 0], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
            ([2], [2])
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                solution.sortColors(nums)
                self.assertEqual(nums, expected)

if __name__ == "__main__":
    unittest.main()
