# Recursion 

In Python, is common for a function to call another function. **In Recursion a  function calls itself**. Most problems beyond academic purposes can be solved without recursion but, there are some some few cases where recursion is the best solution, i.e.:

1. When the problem can be divided into smaller subproblems that are identical to the original problem AND the recursion depth is not too deep. How deep might you ask yourself? It basically depends on the large of your data and the amount of memory available. If you don't know how deep the recursion will go, you can always use a loop instead.

    examples: 
    Hierarchical data structures, like trees, file systems, organizational charts,graphs, etc.
    Traversing a tree, like in a depth-first search.
    Parsing and processing nested structures, like JSON, XML, etc.

2. Divide and conquer algorithms, like merge sort, quick sort, binary search, etc. These are usually more clearly expressed using recursion.

## Basics of recursion in Python

1 - **Base case**: The stopping condition preventing an infinite loop.
2 - **Recursive step**: Calling the function with a modified parameter that moves towards the base case.

Below you can see a common example of recursion that is taught in most programming courses, the factorial function.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

A factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!.

- 0 is the `base case`, the termination condition
- Each call of the function reduces the number of iterations by 1, moving towards the base case.

As we mention, recursion has its pitfalls, the pretty obvious one here is `forgetting to set up a base case`. In this particular case, the multiplication will stop at 0 or 1 without the need to explicitly set a base case. **Note** that this is not always the case, and you should always set up a base case when possible. Forgetting the base case leads to a `stack overflow`, basically the program will run oom - out of memory.

Another common pitfall is not `properly propagating the return values`. This means that you are not using the return value of the recursive call and/or passing it to the next recursive call. Worry not, this is fairly common when you are starting with recursion, and you will get the hang of it with practice.

## Recursion practice - easy

Implement tehse recursive functions and remember:

- First, identify the base case.
- Then, test your functions with edge cases, empty imputs, 0, 1, single element, etc.
- When stuck, write the logic for 2-3 small cases in a structured way to identify the pattern.

1. Sum of digits
Hint: Use modulo and integer division

2. List element count
Hint: Slice the list progressively

3. Palindrome checker
Hint: Compare first/last characters and reduce string

4. Power function (x^n)
Hint: x^n = x * x^(n-1)

5. Fibonacci sequence
Hint: fib(n) = fib(n-1) + fib(n-2)

6. Greatest Common Divisor (GCD)
Hint: Use Euclid's algorithm

7. Binary search
Hint: Split array and compare middle element

8. Directory tree traversal
Hint: Use os.listdir() and os.path.isdir()

9. String reversal
Hint: Take last character + reverse remaining

10. Tower of Hanoi solver
Hint: Move n-1 disks, then move largest disk