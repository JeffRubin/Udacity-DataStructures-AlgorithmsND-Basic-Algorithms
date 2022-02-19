# Problem 5: Autocomplete With Tries

## Description
Copied the notebook in problem_5.py.  The notebook specified design choices for the design of the trie and the
implementation of autocomplete via implementation of trie find() for a specified prefix and implementation of
trie node suffixes() given the prefix (recursive search for suffixes that are the autocompletions).

## Complexity: Time
O(n) to find all the suffixes since to find these essentially have to traverse the tree formed by the trie; traversing a
non-orderd tree has a time complexity of O(n) since have to visit all nodes.

## Complexity: Space
O(n) to find all the suffixes since to find all the suffixes requires a recursive call of suffixes() which
essentially traverses a tree formed by the trie.  In the worst case that the tree is very unbalanced the depth of the
recursive call stack is thus O(n).
