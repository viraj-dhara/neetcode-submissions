# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # remove null lists
        new_lists = []
        for item in lists :
            if item is not None :
                new_lists.append(item) 
        lists = new_lists

        # simple edge cases
        if len(lists) == 0 : return None
        if len(lists) == 1 : return lists[0]
        
        # actual code
        curr = ListNode()
        combined_sorted = curr
        myheap = list()

        for i, item in enumerate(lists) :
            heapq.heappush(myheap, (item.val, i))

        while True :
            
            if not myheap : break
            
            curr.next = ListNode()
            curr = curr.next

            curr.val, index = heapq.heappop(myheap)
            
            lists[index] = lists[index].next
            if lists[index] is not None :
                heapq.heappush(myheap, (lists[index].val, index))


        
        return combined_sorted.next




