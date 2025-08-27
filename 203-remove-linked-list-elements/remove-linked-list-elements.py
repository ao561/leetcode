# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer = dummy

        while pointer:
            while pointer.next and pointer.next.val == val:
                pointer.next = pointer.next.next
            pointer = pointer.next

        return dummy.next