# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        slow = head

        while slow != None :
            size += 1
            slow = slow.next

        if size == n : return head.next

        slow = head
        for i in range(size - n - 1) :
            slow = slow.next
        
        slow.next = slow.next.next if slow.next is not None else None

        return head
        