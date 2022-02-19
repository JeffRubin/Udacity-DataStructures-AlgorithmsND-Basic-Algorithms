# Problem 7: Request Routing In A Web Server With A Trie

## Description
The problem specified design choices for the design of the trie to implement an HTTPRouter that returns a handler for
a specified URL path.  This is similar to problem 5 - Autocomplete With Tries, except in the current problem path parts,
e.g. "home", "about", are used as the keys for the dictionary of the trie node's children instead of characters,
e.g. 'a','b'.

## Complexity: Time
O(n) to return a handler since to find this essentially have to traverse the tree formed by the trie; traversing a
non-orderd tree has a time complexity of O(n) since have to visit all nodes.

## Complexity: Space
O(1) to return a handler since loop through the trie to find the specified URL path and return the associated handler
(if it exists).  Just need space for cur_node to achieve this search.
