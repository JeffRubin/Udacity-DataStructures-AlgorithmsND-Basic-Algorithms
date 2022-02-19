# Problem 1: Square Root Of An Integer

## Description
Used a binary search to find the square root approximation where the ordered list to binary search is the list from
[0, number] where number is the number for which to find the square root approximation.  Unlike a traditional binary
search where subsequent recursive searches exclude the midpoint, I choose to keep the midpoint in subsequent recursive
searches (e.g. if the midpoint is 8 the next recursive call uses 8 instead of 7 or 9) since this results in faster
results when the number is an even perfect square (e.g. 16 --> 8 --> 4, finds the square root in 2 steps).

## Complexity: Time
O(log n) since used a binary search to find the square root approximation; this splits the search space in half on
each recursive call.

## Complexity: Space
O(log n) since the space complexity is driven by the depth of the recursive call stack which is O(log n)
since used a binary search to find the square root approximation.  The amount of memory per each recursive call is
constant, i.e. storage for mid and sqrt_approx so the depth of call stack is really what drives memory utilization.
