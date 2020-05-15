"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
class Trie:

    def __init__(self):
        self.isEndOfWord = False
        self.children = [None] * 26
        
    def insert(self, word: str) -> None:
        curr = self;
        for c in word:
            if curr.children[ord(c)- ord('a')] == None:
                curr.children[ord(c)- ord('a')] = Trie()
            curr = curr.children[ord(c)- ord('a')]
        curr.isEndOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            curr = curr.children[ord(c)- ord('a')]
            if curr == None:
                return False
        if(curr.isEndOfWord):
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            curr = curr.children[ord(c)- ord('a')]
            if curr == None:
                return False
        return True
