# Problem 4: Dutch National Flag Problem

## Description
The approach was to in-place sort 0s and 2s in a single traversal by bringing all 0s to the front of the input array and
all 2s to the end of the input array.  A result of this is that all 1s end up between the 0s and 2s in the array.

This is the same problem as Sort 0, 1, 2 in Lesson 2: Sorting Algorithms.  I did that exercise while going through the
lesson.  I recreated a solution here without looking at my previous work to test my understanding; I verified the final
result against the earlier work.

## Complexity: Time
O(n) in a single traversal.

## Complexity: Space
O(1), just the local variables, e.g. next 0 and 2 indices, current value.
