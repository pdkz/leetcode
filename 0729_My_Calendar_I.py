class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, start, end):
        if not self.root :
            self.root = Node(start, end)
            return True
        return self._insert(self.root, start, end)

    def _insert(self, node, start, end):
        if end <= node.start:
            if not node.left:
                node.left = Node(start, end)
                return True
            else:
                return self._insert(node.left, start, end)
        elif start >= node.end:
            if not node.right:
                node.right = Node(start, end)
                return True
            else:
                return self._insert(node.right, start, end)
        return False

class MyCalendar:
    def __init__(self):
        self.bst = BinarySearchTree()

    def book(self, start: int, end: int) -> bool:
        if not self.bst:
            self.bst = BinarySearchTree()
        return self.bst.insert(start, end)
