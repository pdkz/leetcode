from collections import deque
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = deque([])
        self.temp = []
        for el in nestedList:
            if el.isInteger():
                self.nums.append(el.getInteger())
            else:
                self.temp.clear()
                self.dfs(el)
                for num in self.temp:
                    self.nums.append(num)

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        if self.nums:
            return True
        return False

    def dfs(self, nested_list):
        if isinstance(nested_list, int):
            self.temp.append(nested_list)
            return
        for l in nested_list.getList():
            if l.isInteger():
                self.temp.append(l.getInteger())
            else:
                self.dfs(l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())