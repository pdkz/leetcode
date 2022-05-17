class Node:
    def __init__(self, char):
        self.char = char
        self.children = [-1] * 26
        self.is_finished = False
        
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(' ')
        
    def _convert_char_to_num(self, char: str) -> int:
        return ord(char) - ord('a')
        
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        
        current = self.root
        
        for char in word:
            char_index = self._convert_char_to_num(char)
            if current.children[char_index] != -1:
                current = current.children[char_index]
            else:
                node = Node(char)
                current.children[char_index] = node
                current = node

        current.is_finished = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not self.root:
            return False
        
        current = self.root
        for char in word:
            char_index = self._convert_char_to_num(char)
            if current.children[char_index] != -1:
                current = current.children[char_index]
            else:
                return False
        if not current.is_finished:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not self.root:
            return False
        
        current = self.root
        for char in prefix:
            char_index = self._convert_char_to_num(char)
            if current.children[char_index] != -1:
                current = current.children[char_index]
            else:
                return False
        return True