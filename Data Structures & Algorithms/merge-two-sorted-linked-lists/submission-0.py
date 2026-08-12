# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged_list = ListNode()
        prev_node = merged_list

        while list1 != None and list2 != None:

            newNode = ListNode()

            if list1.val < list2.val :
                newNode.val = list1.val
                list1 = list1.next
            else :
                newNode.val = list2.val
                list2 = list2.next
            
            prev_node.next = newNode
            prev_node = newNode

        if list1 != None:
            prev_node.next = list1
        elif list2 != None:
            prev_node.next = list2

        return merged_list.next

