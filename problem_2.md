# Problem 2: Search In A Rotated Sorted Array

## Description
Used a binary search to find the rotation pivot then used another binary search for the specified target in the ordered
list that either: starts at the pivot or ends right before the pivot (i.e. split out the ordered lists that are
divided by the pivot and then performed a binary search for the target in the appropriate one of those lists).

## Complexity: Time
O(log n) since the binary search to find the pivot is O(log n) and then the binary search for the target in the
appropriate ordered list is O(log n).  Note that O(2log n) ~ O(log n).

## Complexity: Space
O(log n) since the space complexity is driven by the depth of the recursive call stack which is O(log n) for both
find_pivot() and binary_search() since these both use binary search.  The amount of memory per each recursive call is
constant, i.e. storage for mid_idx and mid_val so the depth of call stack is really what drives memory utilization.
Since find_pivot() is called first and then its call stack completely returns before binary_search() is called,
no more than O(log n) memory is used at a time.
