from collections import deque

#use binary search to find the peak element
def peak_element(arr):
    low = 0
    high =  len(arr) - 1
    def binary_search(arr, low, high):    
        mid = (low + high) // 2

        left = float('-inf')
        right = float('-inf')

        if mid -1 >= 0:
            left = arr[mid-1]
        if mid + 1 <= len(arr) - 1:
            right = arr[mid+1]

        if arr[mid] > left and arr[mid] > right:
            return mid
        elif left > right:
            return binary_search(arr, low, mid-1)
        else:
            return binary_search(arr, mid+1, high)

    return binary_search(arr, low, high)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 11, 7, 8, 9, 6]
    print(peak_element(arr))
