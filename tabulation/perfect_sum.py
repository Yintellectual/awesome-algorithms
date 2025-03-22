#count all subsets of the array whose sum is equal to the given target.
#Given an array arr of non-negative integers and an integer target

def perfectSum(arr, target):
    # code here
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in arr:
        if num > target:
            continue
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[target]
if __name__ == "__main__":
    arr1 = [5, 2, 3, 10, 6, 8]
    target1 = 10
    arr2 = [2, 5, 1, 4, 3]
    target2 = 10
    print(f"Number of perfect sums ={perfectSum(arr2, target2)}")
