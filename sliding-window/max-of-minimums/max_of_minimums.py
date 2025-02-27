import logging

def max_of_minimums(arr):
    n = len(arr)
    stack = []
    left = [-1] * n
    right = [n] * n
    logging.basicConfig(level=logging.DEBUG)
    # The highland by an index is the range where the elements are greater than the element at that index. 
    # Each highland have a left and right boundary, exclusively.

    # Update left boundary of each highland
    # find the nearest element on the left that is less than the current element
    # those elements to the left of the left boundary are irrelavent to the current element

    # the key is to use a stack to keep track of the elements that are candidates for the left boundary
    # once we found a smaller candidates, the previous candidates are no longer needed
    
    for i in range(n):
        while(stack and arr[stack[-1]] >= arr[i]):
             stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

        # Replace print statements with logging.debug
    logging.debug(f"{'Left boundaries:':<20} {left}")
    # Update right boundary of each highland
    stack = []
    for i in range(n-1, -1, -1):
        while(stack and arr[stack[-1]] >= arr[i]):
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    
    logging.debug(f"{'Right boundaries:':<20} {right}")
    
    # Calculate the size of highland for each element
    highland_size = [0] * n
    for i in range(n):
        highland_size[i] = right[i] - left[i] - 1
    
    logging.debug(f"{'Highland sizes:':<20} {highland_size}")

    # Calculate the maximum of the minimums
    result = [0] * n
    for i in range(n):
        k = highland_size[i]
        result[k-1] = max(result[k-1], arr[i])
    
    logging.debug(f"{'Result:':<20} {result}")

    # Fill the missing values
    for i in range(n-2, -1, -1):
        result[i] = max(result[i], result[i+1])

    logging.debug(f"{'Final result:':<20} {result}")

if __name__ == "__main__":
    sample = [20, 30, 40, 10, 30]
    max_of_minimums(sample)
