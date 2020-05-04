Time complexity:

1. For building a Trie: O(n*m), as we need to iterate over 
each string (n is the average string length) in string array 
(of length equal to m).
2. For finding a prefix: O(n), as we need to follow trie branches
for every letter in prefix.
3. For finding all suffixes: O(n*m), as we need to go through all
letters in every word in the node, which in the worst case 
scenario is trie root.

Time complexity of complete finding suffix algorithm is therefore
O(n*m)

Space complexity:

Algorithm operates on Trie data structure, which has the biggest
memory footprint of all operations. Its time complexity
is O(m*n) in the worst case scenario (no word in trie shares a
prefix), where m is the number of words and n is average number of 
characters in word.