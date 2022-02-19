# Problem 7: Request Routing In A Web Server With A Trie

## Description
The problem statement specified design choices for the design of the trie to implement an HTTPRouter that returns a
handler for a specified URL path.  This is similar to problem 5 - Autocomplete With Tries, except in the current problem
path parts, e.g. "home", "about", are used as the keys for the dictionary of the trie node's children instead of
characters, e.g. 'a','b'.

## Complexity: Time
* Insert/Find: O(n) where n is the number of parts in the path since, in the worst case, have to traverse all
parts of the path to insert the whole path or search for it.

## Complexity: Space
* Create Trie: O(n*m) where n is the number of paths represented in the trie and m is the average number of parts in
each path.  Assuming n >> m this is O(n).
* Insert Path: O(n) where n is the number of parts in the path since, in the worst case, have to insert all
parts of the path into the trie.
* Find A Path: O(1) since only need to keep track of the current trie node while searching.  A handler is returned
as a result of the search which is O(1) since it's a string of fixed length for the name of the handler.
