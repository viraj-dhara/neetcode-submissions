# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next == None or head.next.next == None : return 

        slow = fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        even_length = 0
        if fast.next != None :
            fast = fast.next
            even_length = 1 
        else :
            ...
        
        lower_middle = slow
        if even_length == 1 : upper_middle = slow.next
        end = fast

        # reversing logic
        curr = slow.next
        future = slow.next.next
        prev = None
        while curr != None :
            curr.next = prev
            prev = curr
            curr = future
            future = future.next if future is not None else None
        
        if even_length == 1 :
            lower_middle.next = upper_middle
            upper_middle.next = None
        else :
            lower_middle.next = None

        curr = head
        future_even = end
        future_odd = head.next
        even_flag = 1
        while curr != lower_middle :

            if even_flag == 1 :
                curr.next = future_even
                future_even = future_even.next if future_even is not None else None
            else :
                curr.next = future_odd
                future_odd = future_odd.next if future_odd is not None else None
            
            even_flag = not even_flag
            curr = curr.next

        return

        