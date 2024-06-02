# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prevents None pointer error- invalid reference when given list is empty
        if head is None:
            return head
        # stopping condition of condition
        # if there is only one item
        #reverse is the same as original list
        if head.next is None:
            return head
        #Creating the second
        second = head.next
        # Reverse the rest of the list
        new_head = self.reverseList(second)
        # head of the original list is not the tail of the new list
        # While it was pointing out the second node, now it is pointing out None
        head.next = None
        # Tail of the reversed list in the sub problem,
        #We assigned the second variable, now it is the tail of the small list that is reversed
        second.next = head
        return new_head


        # prev = None
        # current = head

        # while current != None:
        #     forward = current.next
        #     current.next = prev
        #     prev = current
        #     current =forward
