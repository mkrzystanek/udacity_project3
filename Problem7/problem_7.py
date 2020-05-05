# HTTPRouter using a Trie


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = "root handler"

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for path in paths:
            current.insert(path)
            current = current.paths[path]
        current.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for p in paths:
            if p not in current.paths:
                return "not found handler"
            current = current.paths[p]
        return current.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.paths = {}
        self.handler = "not found handler"

    def insert(self, path):
        if path not in self.paths:
            self.paths.update({path: RouteTrieNode()})


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path is None:
            return 'not found handler'
        path_parts = self.split_path(path)
        return self.route_trie.find(path_parts)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        paths = path.split("/")
        paths = list(filter(lambda p: p != "", paths))
        return paths


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router()
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
assert router.lookup("/") == 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
assert router.lookup("/home") == 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
assert router.lookup("/home/about") == 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
assert router.lookup("/home/about/") == 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
assert router.lookup("/home/about/me") == 'not found handler'
print(router.lookup(""))  # prints 'root handler'
assert router.lookup("") == 'root handler'
print(router.lookup("//"))  # prints 'root handler'
assert router.lookup("//") == 'root handler'
print(router.lookup("/about"))  # prints 'not found handler'
assert router.lookup("/about") == 'not found handler'
print(router.lookup(None))  # prints 'not found handler'
assert router.lookup(None) == 'not found handler'
