# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        curr_result_node = ListNode(val=0)
        new_head = prev_result_node = curr_result_node
        flag_a = True 
        flag_b = True

        while (l1 != None and l2 != None) and (flag_a == True or flag_b == True) :
            
            curr_digit = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            curr_result_node = ListNode(val=curr_digit)
            prev_result_node.next = curr_result_node
            prev_result_node = curr_result_node

            l1 = l1.next
            l2 = l2.next

            if l1 == None :
                flag_a = False
                l1 = ListNode(val = 0, next = None)
                l1.next = l1
            if l2 == None :
                flag_b = False
                l2 = ListNode(val = 0, next = None)
                l2.next = l2

        if carry != 0 :
            curr_result_node.next = ListNode(val=carry)
            

        return new_head.next
        
