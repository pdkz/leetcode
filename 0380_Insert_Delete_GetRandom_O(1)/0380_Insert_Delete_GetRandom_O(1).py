import random
class RandomizedSet:
    def __init__(self):
        self.values = {}
        self.choice = []
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False

        self.len += 1
        self.choice.append(val)
        self.values[val] = self.len - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False

        idx = self.values[val]
        self.choice[idx] = self.choice[-1]
        self.values[self.choice[-1]] = idx
        self.choice.pop()
        del self.values[val]
        self.len -= 1

        return True

    def getRandom(self) -> int:
        v = random.randint(0, self.len - 1)
        return self.choice[v]