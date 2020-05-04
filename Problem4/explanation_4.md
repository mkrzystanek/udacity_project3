sort_012() function sorts input list in one traversal, so it takes
O(n) iterations to finish. Inside, it uses few list operations
like pop(), which have time complexity of O(n) as well. Therefore,
the final time complexity of the algorithm is O(n^2).

Algorithm only operates on input list and variables that are 
independent of input. Therefore space complexity is O(n).