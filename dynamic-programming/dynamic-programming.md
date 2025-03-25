# Dynamic Programming (DP)

**Dynamic Programming(DP)** caches solutions to subproblems to optimize computation. 

Suppose solution of problem A is combination of subproblems B and A-B, B is C and B-C and so on. We cache solutions of all subproblems, so that some of the subproblems can be reused. The input is consumed one by one, each time we update the solutions of relevent subproblems. Once the input is completed consumed, the solution of problem A reveal itself. 

---

## Memorization vs Tabulation

When we update the cache recursively, it is called **Memorization**. When we update the cache interationaly, it is called **Tabulation**. 

---

## Classic Applications

- 0/1 Knapsack
- Fibonacci

---

## Conventions

The cache is usually named as `dp`. Usually the `dp` is an array or a hash table