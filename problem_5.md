# Problem 5: Autocomplete With Tries

## Description
Copied the notebook in problem_5.py.  The notebook specified design choices for the design of the trie and the
implementation of autocomplete via implementation of trie find() for a specified prefix and implementation of
trie node suffixes() given the prefix (recursive search for suffixes that are the autocompletions).

## Complexity: Time
* Insert/Find: O(n) where n is the number of characters in the word since, in the worst case, have to traverse all
characters of the word to insert the whole word or search for it.
* Autocomplete: O(n*m) where n is the number of words that begin with the specified prefix and m is the average length
of each of those words since have to recurse through all nodes of a tree starting with the node at the specified prefix.
Assuming n >> m this is O(n).

## Complexity: Space
* Create Trie: O(n*m) where n is the number of words represented in the trie and m is the average length of each word.
Assuming n >> m this is O(n).
* Insert Word: O(n) where n is the number of characters in the word since, in the worst case, have to insert all
characters of the word into the trie.
* Find A Word: O(1) since only need to keep track of the current trie node while searching.  A node is also returned
as a result of the search which is also O(1).
* Autocomplete: O(n) where n is the maximum length of a word starting with the specified prefix since this is the 
maximum depth of the call stack for the recursive calls to find all the suffixes.
