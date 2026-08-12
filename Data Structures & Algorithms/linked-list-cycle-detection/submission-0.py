# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None or head.next.next == None : return False
        if head.next == head or head.next.next == head : return True

        slow = head.next
        fast = head.next.next

        while fast != None and fast.next != None :
            if fast == slow : return True
            slow = slow.next
            fast = fast.next.next

        return False