# Problem 5: Autocomplete With Tries

## Description
Copied the notebook in problem_5.py.  The notebook specified design choices for the design of the trie and the
implementation of autocomplete via implementation of trie find() for a specified prefix and implementation of
trie node suffixes() given the prefix (recursive search for suffixes that are the autocompletions).

## Complexity: Time
* TrieNode
  * __init__(self): O(1) since just initializing member attributes for a single instance of TrieNode
  * insert(self, char): O(1) since just creating a single entry in the children dictionary (entry is a single instance
  of TrieNode)
  * suffixes(self, suffix=''): O(n*m) where n is the number of words that begin after the node on which this method is
  called and m is the average length of each of those words (starting after the node on which this method is
  called) since have to recurse through all nodes of a tree starting after the node on which this method is called.
  Assuming n >> m this is O(n).
* Trie
  * __init__(self): O(1) since just creating the root node (a single instance of TrieNode)
  * insert(self, word): O(n) where n is the number of characters in the word since have to traverse all characters of
  the word to insert the whole word.
  * find(self, prefix): O(n) where n is the number of characters in the word since, in the worst case, have to traverse
  all characters of the word to search for it.
  * autocomplete(self, prefix): O(n) to find the prefix node.  O(n*m) where n is the number of words that begin with the
  specified prefix and m is the average length of each of those words (excluding the length of the prefix) since have to
  recurse through all nodes of a tree starting with the node at the specified prefix. Assuming n >> m this is also O(n)
  so the overall time complexity is still O(n).

## Complexity: Space
* TrieNode
  * __init__(self): O(1) since just creating a single TrieNode instance
  * insert(self, char): O(1) since just creating a single TrieNode child instance
  * suffixes(self, suffix=''): O(n) where n is the maximum length of a word that begins after the node on which this
  method is called since this is the maximum depth of the call stack for the recursive calls to find all the suffixes.
  The output list of suffixes is O(n*m) where n is the number of words that begin after the node on which this
  method is called and m is the average length of each of those words (excluding the length of the prefix).
  Assuming n >> m this is also O(n) so the overall space complexity is still O(n).
* Trie
  * __init__(self): O(1) since just creating a single TrieNode instance for the root.
  * insert(self, word): O(n) where n is the number of characters in the word since, in the worst case, have to insert
  TrieNode instances for all characters of the word into the trie.
  * find(self, prefix): O(1) since only need to keep track of the current trie node while searching.  A node is also
  returned as a result of the search which is also O(1).
  * autocomplete(self, prefix): O(n) where n is the maximum length of a word that begins after the prefix since this is
  the maximum depth of the call stack for the recursive calls to find all the suffixes.  Note that the output list of
  suffixes is O(n*m) where n is the number of words that begin after the prefix and m is the average length of each of
  those words (excluding the length of the prefix).  Assuming n >> m this is also O(n) so the overall space complexity
  is still O(n).  Note that the space complexity is O(1) for the prefix node when this if found at the beginning of this
  method, however, this is minor compared to the other space complexity of this method.
