class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
            
    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.endOfWord = True

    def startsWith(self, word: str) -> bool:
        curr = self.root

        for char in word:
        
            if char not in curr.children:
                return False
        
            curr = curr.children[char]
            
        return True
    
    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
        
            if char not in curr.children:
                return False
        
            curr = curr.children[char]
        
        return curr.endOfWord 

# Time: O(n)
# Space: O(1)