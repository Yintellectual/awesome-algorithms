# Max of Minimums in Sliding Window

## Introduction
This algorithm finds the maximum of the minimum values in all sliding windows of different sizes for a given array. It uses a stack-based approach to efficiently compute the left and right boundaries for each element, which helps in determining the size of the "highland" (subarray) for each element.

## Algorithm Explanation

### Step 1: Initialize Boundaries
- **Left Boundaries**: An array to store the nearest smaller element's index on the left for each element.
- **Right Boundaries**: An array to store the nearest smaller element's index on the right for each element.

### Step 2: Compute Left Boundaries
- Use a stack to keep track of indices of elements.
- For each element, pop elements from the stack until the top of the stack is smaller than the current element.
- The top of the stack is the nearest smaller element on the left.
- Push the current element's index onto the stack.

### Step 3: Compute Right Boundaries
- Reset the stack.
- Iterate from the end of the array to the beginning.
- For each element, pop elements from the stack until the top of the stack is smaller than the current element.
- The top of the stack is the nearest smaller element on the right.
- Push the current element's index onto the stack.

### Step 4: Calculate Highland Sizes
- For each element, the size of the highland is determined by the difference between the right and left boundaries.

### Step 5: Calculate Maximum of Minimums
- Initialize a result array to store the maximum of minimums for each window size.
- For each element, update the result array with the maximum value for the corresponding highland size.

### Step 6: Fill Missing Values
- Ensure that the result array is filled by propagating the maximum values to smaller window sizes.

## Example
Given the array `[20, 30, 40, 10, 30]`, the algorithm will compute the maximum of minimums for all sliding windows of different sizes.

## Code
```python
import logging

def max_of_minimums(arr):
    n = len(arr)
    stack = []
    left = [-1] * n
    right = [n] * n
    logging.basicConfig(level=logging.DEBUG)

    for i in range(n):
        while(stack and arr[stack[-1]] >= arr[i]):
             stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    logging.debug(f"{'Left boundaries:':<20} {left}")

    stack = []
    for i in range(n-1, -1, -1):
        while(stack and arr[stack[-1]] >= arr[i]):
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    
    logging.debug(f"{'Right boundaries:':<20} {right}")
    
    highland_size = [0] * n
    for i in range(n):
        highland_size[i] = right[i] - left[i] - 1
    
    logging.debug(f"{'Highland sizes:':<20} {highland_size}")

    result = [0] * n
    for i in range(n):
        k = highland_size[i]
        result[k-1] = max(result[k-1], arr[i])
    
    logging.debug(f"{'Result:':<20} {result}")

    for i in range(n-2, -1, -1):
        result[i] = max(result[i], result[i+1])

    logging.debug(f"{'Final result:':<20} {result}")

if __name__ == "__main__":
    sample = [20, 30, 40, 10, 30]
    max_of_minimums(sample)
```

## Conclusion
This algorithm efficiently computes the maximum of minimum values for all sliding windows of different sizes using a stack-based approach to determine the boundaries of each element's highland.