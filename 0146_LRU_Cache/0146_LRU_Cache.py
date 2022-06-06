class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        """
        left(LRU) <-prev right(most recent)
                  ->next
        """

    def insert(self, node):
        """
        Insert at most right point
                         prev
        left <-> ... <-> node <-> right
                                  next
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # To most right node
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        # To most right node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.defaultdict(int)
        self.ref_counter = collections.defaultdict(int)
        self.count = 0

    def get(self, key: int) -> int:
        if self.cache.get(key) == None:
            return -1

        self.ref_counter[key] = self.count
        self.count += 1

        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.cache[key] = value
            self.ref_counter[key] = self.count
            self.count += 1
            return

        if len(self.cache) >= self.capacity:
            #print(key, self.ref_counter)
            min_k = min(self.ref_counter, key=self.ref_counter.get)
            del self.ref_counter[min_k]
            del self.cache[min_k]

        self.cache[key] = value
        self.ref_counter[key] = self.count
        self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
