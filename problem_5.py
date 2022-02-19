# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for all complete words below this point
        collected_suffixes = []

        if len(suffix) > 0 and self.is_word:
            collected_suffixes.append(suffix)

        for c in self.children:
            collected_suffixes += self.children[c].suffixes(suffix + c)

        return collected_suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                cur_node.insert(c)

            cur_node = cur_node.children[c]

        cur_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        cur_node = self.root

        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return None

        return cur_node

    def autocomplete(self, prefix):
        prefix_node = self.find(prefix)
        if prefix_node is None:
            return None
        else:
            suffixes = prefix_node.suffixes()
            if len(suffixes) > 0:
                return suffixes
            else:
                return None

# Test Cases
#
# Trie for nominal test cases
Trie_Nominal = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    Trie_Nominal.insert(word)
#
# Test Case 1: Prefix is not a word
print(Trie_Nominal.autocomplete('a'))
# Expected Output: ['nt', 'nthology', 'ntagonist', 'ntonym']
#
# Test Case 2: Prefix is a word - Other words exist that are longer than the prefix
print(Trie_Nominal.autocomplete('ant'))
# Expected Output: ['hology', 'agonist', 'onym']
#
# Test Case 3: Prefix is a word - No other words exist that are longer than the prefix
print(Trie_Nominal.autocomplete('function'))
# Expected Output: None
#
# Test Case 4: Prefix matches only 1 entry in the word list
print(Trie_Nominal.autocomplete('fa'))
# Expected Output: ['ctory']
#
# Test Case 5: Edge Case: Empty prefix (prefix matches all entries in the word list)
print(Trie_Nominal.autocomplete(''))
# Expected Output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
#
# Test Case 6: Edge Case: Prefix matches no entries in the word list
print(Trie_Nominal.autocomplete('zzz'))
# Expected Output: None
#
# Test Case 7: Edge Case: Empty Trie
Trie_Empty = Trie()
print(Trie_Empty.autocomplete('a'))
# Expected Output: None
