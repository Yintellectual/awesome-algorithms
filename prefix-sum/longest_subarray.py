#for subarrays with sum equal to k, 
#find the longest subarray
#return its length

def longest_subarray(arr, k):
    sum_dict = {}
    current_sum = 0
    max_length = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == k:
            max_length = max(max_length, i + 1)
        if current_sum - k in sum_dict:
            max_length = max(max_length, i - sum_dict[current_sum - k])
        if current_sum not in sum_dict:
            sum_dict[current_sum] = i 
    return max_length
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 5
    print(longest_subarray(arr, k))
