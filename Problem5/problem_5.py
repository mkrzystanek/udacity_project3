class TrieNode:
    """Represents a single node in the Trie"""
    def __init__(self):
        """Initialize this node in the Trie"""
        self.children = {}
        self.is_word = False

    def insert(self, char):
        """Add a child node in this Trie"""
        if char not in self.children:
            self.children.update({char: TrieNode()})

    def suffixes(self):
        return self._suffixes([], "")

    def _suffixes(self, suffixes, suffix):
        """Recursive function that collects the suffix for all complete words below this point"""
        if self.is_word and suffix is not "":
            suffixes.append(suffix)
        if len(self.children) == 0:
            return
        for char in self.children:
            new_suffix = suffix + char
            self.children[char]._suffixes(suffixes, new_suffix)
        return suffixes


class Trie:
    """The Trie itself containing the root node and insert/find functions"""
    def __init__(self):
        """ Initialize this Trie (add a root node)"""
        self.root = TrieNode()

    def insert(self, word):
        """Add a word to the Trie"""
        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        """Find the Trie node that represents this prefix"""
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefix = MyTrie.find("a")
print(prefix.suffixes())
assert set(prefix.suffixes()) == {'nt', 'nthology', 'ntagonist', 'ntonym'}
prefix2 = MyTrie.find("fun")
print(prefix2.suffixes())
assert set(prefix2.suffixes()) == {'ction'}
prefix3 = MyTrie.find("tripod")
print(prefix3.suffixes())
assert prefix3.suffixes() is None
prefix4 = MyTrie.find("z")
assert prefix4 is None

MyTrie2 = Trie()
prefix5 = MyTrie2.find("a")
assert prefix5 is None