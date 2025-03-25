def knapsack(w, val, wt):
    dp = [0]*(w+1)
    optimized_combination = [""]*(w+1)
    for i in range(len(wt)):
        weight = wt[i]
        if(weight > w):
            continue

        for j in range(w, weight-1, -1):
            old_value = dp[j]
            new_value = dp[j-weight] + val[i]
            dp[j] = max(old_value, new_value)
            optimized_combination[j] = optimized_combination[j-weight] + f"({wt[i]},{val[i]}) "
        
    return dp[w], optimized_combination[w]



if __name__ == "__main__":
    W = 5
    val = [10, 40, 30, 50]
    wt = [5, 4, 2, 3] 
    print(knapsack(W, val, wt))


        

