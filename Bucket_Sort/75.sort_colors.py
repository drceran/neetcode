from typing import List

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        max_value = max(nums)
        counts_list = (max_value+1) * [0]


        # n = 0 1 2 3 4 5
        for num in nums:
            counts_list[num] +=1

        i = 0

        for num in range(len(counts_list)):
            for _ in range(counts_list[num]):
                nums[i] = num
                i +=1

