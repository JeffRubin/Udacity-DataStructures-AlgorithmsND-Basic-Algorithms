class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, path_part):
        self.children[path_part] = RouteTrieNode()


# RouteTrie stores routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts, handler):
        cur_node = self.root

        for part in path_parts:
            if part not in cur_node.children:
                cur_node.insert(part)

            cur_node = cur_node.children[part]

        cur_node.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur_node = self.root

        for part in path_parts:
            if part not in cur_node.children:
                return None
            else:
                cur_node = cur_node.children[part]

        return cur_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.routes = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        self.routes.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler

        # remove trailing slash
        if len(path) > 0 and path[-1] == "/":
            path = path[:-1]

        handler = self.routes.find(self.split_path(path))

        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        if len(path) == 0:
            return []

        path_parts = path.split('/')
        if path[0] == '/':
            path_parts = path_parts[1:] # first part is an empty string, the empty string before the first /
        return path_parts

# Test Cases
#
# Router and route for nominal test cases
router_nominal = Router("root handler", "not found handler")
router_nominal.add_handler("/home/about", "about handler")  # add a route
#
# Test Case 1: Non-root path, handler exists
print(router_nominal.lookup("/home/about"))
# Expected Output: 'about handler'
#
# Test Case 2: Non-root path, handler does not exist, sub-path of a valid path
print(router_nominal.lookup("/home"))
# Expected Output: 'not found handler'
#
# Test Case 3: Non-root path, handler does not exist, super-path of a valid path
print(router_nominal.lookup("/home/about/abc"))
# Expected Output: 'not found handler'
#
# Test Case 4: Non-root path, handler does not exist, completely invalid path
print(router_nominal.lookup("/abc/def"))
# Expected Output: 'not found handler'
#
# Test Case 5: Root path
print(router_nominal.lookup("/"))
# Expected Output: 'root handler'
#
# Test Case 6: Edge Case: Root path with no trailing slash
print(router_nominal.lookup(""))
# Expected Output: 'root handler'
#
# Test Case 7: Edge Case: Non-root path with a trailing slash
print(router_nominal.lookup("/home/about/"))
# Expected Output: 'about handler'
#
# Router for no route test cases (all edge cases)
router_no_routes = Router("root handler", "not found handler")
# do not add any routes
#
# Test Case 8: Edge Case: Root path
print(router_no_routes.lookup("/"))
# Expected Output: 'root handler'
#
# Test Case 9: Edge Case: Non-root path, handler does not exist
print(router_no_routes.lookup("/abc"))
# Expected Output: 'not found handler'
