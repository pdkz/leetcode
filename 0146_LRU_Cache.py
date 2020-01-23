class LRUCache:
    
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
