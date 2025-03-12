# Hash Map with Prefix Sum
Given an array of integers `arr` and a target integer `k`, we are interested in finding subarrays whose sum equals `k`.

## Naive Approach:
Loop through all possible subarrays and check if their sum equals k.

**Time complexity: `O(n²)`**, as there are O(n²) subarrays in an array of size n.

## Optimized Approach (Hash Map with Prefix Sum):

Loop through the array once:

Keep track of the current **prefix sum** (sum of elements from `arr[0]` to the current element `arr[i]`).

Use a hash map to store the prefix sum as the key and its corresponding index as the value.

For each element:

First comparison: Check if the current prefix sum equals `k`. If so, update the result.

Second comparison: Check if `(current prefix sum - k)` exists in the hash map. If it does, it means there is a subarray between the index stored in the hash map and the current index whose sum is `k`.

Update the hash map:

If the current prefix sum is not already in the hash map, store it with its index.

**Time Complexity:`O(n)`**, as we only loop through the array once, and hash map lookups/insertions are O(1) on average.

---

Key Insight:
The difference between two prefix sums (current prefix sum - k) gives the sum of a subarray. If this difference exists in the hash map, it means there is a subarray with sum k.