Time complexity:

1. For building a Trie: O(m*n), because we need to save every 
path part - elements of the path separated by "/" (m) -
for every path (n).
2. For looking up a path: O(m), where m is number of path parts.

Space complexity:

Trie data structure space complexity can be classified as O(m*n),
which is number of saved paths times average number of path parts.