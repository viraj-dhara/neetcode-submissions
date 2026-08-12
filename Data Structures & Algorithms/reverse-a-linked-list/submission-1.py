# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None : return head
        stack = deque()
        stack.append(head.val)

        while head.next != None :
            stack.append(head.next.val)
            head = head.next

        new_LL = ListNode(val=stack.pop())
        lastNode = new_LL
        while stack:
            newNode = ListNode(val=stack.pop())
            lastNode.next = newNode
            lastNode = newNode

        return new_LL
