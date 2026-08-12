"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None : return None
        if head.next == None : 
            new = Node(head.val, None, None)
            new.random = new if head.random is not None else None
            return new

        curr = head
        random_ptr_indices = list()
        original = list()
        new = list()
        ptr_to_index = dict()

        indice = 0
        while curr != None :
            ptr_to_index[curr] = indice
            original.append(curr)
            curr = curr.next
            indice += 1

        #calculate indices for random ptrs
        for item in original :
            item.random = ptr_to_index[item.random] if item.random is not None else None
        
        # create new nodes
        for item in original :
            temp = Node(item.val, None, item.random)
            new.append(temp)


        # convert indices to ptrs
        for i, item in enumerate(new) :
            item.random = new[item.random] if item.random is not None else None
            item.next = new[i+1] if i != len(new) - 1 else None

        return new[0]