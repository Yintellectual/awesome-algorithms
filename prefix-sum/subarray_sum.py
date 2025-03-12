#find the subarray with sum equal to target
#return the first and last index of the subarray(1-based index)
#if not found, return [-1]

def subarray_sum(arr, target):
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == target:
                return [i+1, j+1]
    return [-1]

def prefix_sum(arr, target):
    sum_dict = {}
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == target:
            return [0, i]
        if current_sum - target in sum_dict:
            return [sum_dict[current_sum - target] + 2,  i + 1]
        if current_sum not in sum_dict:
            sum_dict[current_sum] = i
    return [-1]



