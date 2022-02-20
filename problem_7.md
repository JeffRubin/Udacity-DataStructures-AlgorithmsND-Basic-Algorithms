# Problem 7: Request Routing In A Web Server With A Trie

## Description
The problem statement specified design choices for the design of the trie to implement an HTTPRouter that returns a
handler for a specified URL path.  This is similar to problem 5 - Autocomplete With Tries, except in the current problem
path parts, e.g. "home", "about", are used as the keys for the dictionary of the trie node's children instead of
characters, e.g. 'a','b'.

## Complexity: Time
* RouteTrieNode
  * __init__(self): O(1) since just initializing member attributes for a single instance of RouteTrieNode
  * insert(self, path_part): O(1) since just creating a single entry in the children dictionary
  (entry is a single instance of RouteTrieNode)
* RouteTrie
  * __init__(self, root_handler): O(1) since just creating the root node (a single instance of RouteTrieNode)
  and its handler.
  * insert(self, path_parts, handler): O(n) where n is the number of path parts since have to traverse all path parts
  to insert the entire path.
  * find(self, path_parts): O(n) where n is the number of path parts since, in the worst case, have to traverse
  all path parts to search for the full path (made up of the path parts).
* Router
  * __init__(self, root_handler, not_found_handler): O(1) since just creates the routes (instance of RouteTrie) and the
  not found handler (handler to use when a specified path is not found)
  * add_handler(self, path, handler): O(n) since this just wraps Router::split_path(self, path) and
  RouteTrie::insert(self, path_parts, handler), both of which are O(n)
  * lookup(self, path): O(n) since this just wraps Router::split_path(self, path) and
  RouteTrie::find(self, path_parts), both of which are O(n) 
  * split_path(self, path): O(n) where n is the number of '/' in the specified path (i.e. ~ the number of path parts)
  since must search for each '/' to split the path at these delimiters.

## Complexity: Space
* RouteTrieNode
  * __init__(self): O(1) since just creating a single RouteTrieNode instance
  * insert(self, path_part): O(1) since just creating a single RouteTrieNode child instance
* RouteTrie
  * __init__(self, root_handler): O(1) since just creating a single RouteTrieNode instance for the root and the root
  handler.
  * insert(self, path_parts, handler): O(n) where n is the number of path parts since, in the worst case, have to insert
  RouteTrieNode instances for all path parts into the trie.
  * find(self, path_parts): O(1) since only need to keep track of the current trie node while searching.  A handler is
  also returned as a result of the search which is also O(1).
* Router
  * __init__(self, root_handler, not_found_handler): O(1) since just creates the routes (instance of RouteTrie) and the
  not found handler (handler to use when a specified path is not found)
  * add_handler(self, path, handler): O(n) since this just wraps Router::split_path(self, path) and
  RouteTrie::insert(self, path_parts, handler), both of which are O(n)
  * lookup(self, path): O(n) since this just wraps Router::split_path(self, path) which is O(n) and
  RouteTrie::find(self, path_parts) which is O(1), so O(n) dominates.
  * split_path(self, path): O(n) where n is the number of path parts since these are all put into a list that is
  returned.
