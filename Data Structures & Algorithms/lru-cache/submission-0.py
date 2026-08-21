class Node:
    def __init__ (self, key, val) :
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        # initialize with size "capacity"
        self.key_node = {}
        self.capacity = capacity 
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node (self, target) :

        target.prev.next = target.next
        target.next.prev = target.prev

    def insert_at_head (self, new_node) :

        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head



    def get(self, key: int) -> int:
        
        # return value for key if exists, else -1

        if key not in self.key_node :
            return -1
        else :
            value = self.key_node[key].val

            self.remove_node(self.key_node[key])
            self.insert_at_head(self.key_node[key])

            return value
        

    def put(self, key: int, value: int) -> None:
        
        # update or add value for key
        # delete least recently used key if "capacity" exceeded
        if key in self.key_node : self.remove_node(self.key_node[key])
        self.key_node[key] = Node(key, value)
        self.insert_at_head( self.key_node[key] )
        
        # print(f"key_node:\n{self.key_node}\nlast node:\n{self.tail.prev.key}")

        if len(self.key_node) > self.capacity:
            del self.key_node[self.tail.prev.key]
            self.remove_node(self.tail.prev)

        # print(f"\npost\nkey_node:\n{self.key_node}\nlast node:\n{self.tail.prev.key}\n\n")
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)