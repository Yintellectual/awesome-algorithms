# Floyd's Cycle-Finding Algorithm (Tortoise and Hare Algorithm)

Floyd's Cycle-Finding Algorithm, also known as the Tortoise and Hare Algorithm, is an efficient way to detect and remove loops in a linked list. It uses two pointers that move at different speeds to identify the presence of a cycle and determine the starting point of the loop.

---
### How it works

A loop will always end the linked list. 

By using 2 pointers:

- Slow Pointer (Tortoise): Moves one step at a time.
- Fast Pointer (Hare): Moves two steps at a time.

If there is a loop, both pointers will meet at node M.

Suppose the loop starts at node L, let 
- a = steps from head to L
- b = steps from L to M
- c = steps from M to L

then we have a+b = m, a + b + c +b = 2m, 
a = c

Therefore, if both pointers meet, then a loop is detected. After then, reset fast to head, change its speed to 1 step a time. Fast and slow will meet again at the starting node of the loop(L). 
