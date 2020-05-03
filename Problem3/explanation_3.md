To find two integers of largest sum in the list of digits, with 
O(n log n) time complexity, I chose to leverage heap sort algorithm.
rearrange_digits() method can be broken down to a few key steps:
1. Build a heap - O(n)
2. Run a loop for every element of the heap - O(n)
3. Inside a loop, take the largest element of the heap - O(log n)

Overall time complexity of rearrange_digits() is :

O(n) + O(n log) = O(n log n).

Building and operating on heap data structure takes O(n) space.
rearrange_digits() also creates two string variables that lengths
are equal to n if added together. Total space taken during execution
of rearrange_digits() is not greater then O(n).