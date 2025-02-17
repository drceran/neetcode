# Definition for a pair.

from typing import List
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    def __str__(self):
        return f"({self.key}, {self.value})"
    

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort_lists(pairs, 0, len(pairs)-1)
        return pairs



    def sort_lists(self, my_list:List, s_index:int, e_index:int):
        if e_index <= s_index:
            return

        #pivot index of the last element
        pivot = e_index
        ust = s_index

        print("Current list is: ", end=None)
        for i in range(s_index, e_index+1):
            print(my_list[i], end=" - ")

        print()
        print(f"Selected pivot is: {my_list[pivot]}")

        # i = 0,1,2,3, len(pairs) - 1
        for alt in range(s_index, e_index):
            if my_list[alt].key <= my_list[pivot].key:

                my_list[alt], my_list[ust] = my_list[ust], my_list[alt]
                ust += 1

        my_list[ust], my_list[pivot] = my_list[pivot], my_list[ust]
    

        self.sort_lists(my_list, s_index, ust-1)
        self.sort_lists(my_list, ust+1, e_index)


pairs = list([Pair(5, "apple"), Pair(9, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")])

Solution().quickSort(pairs)

for element in pairs:
    print(element)

