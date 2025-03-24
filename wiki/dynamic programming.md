
# Dynamic Programming

## Definition
[[Dynamic programming]] is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where the solution can be constructed from solutions to subproblems. Dynamic programming is characterized by two main properties: **optimal substructure** and **overlapping subproblems**.

## Key Concepts

### 1. Optimal Substructure
A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions of its subproblems. This property allows for the recursive formulation of the problem.

### 2. Overlapping Subproblems
A problem has overlapping subproblems if the same subproblems are solved multiple times during the computation of the overall solution. Dynamic programming takes advantage of this by storing the results of subproblems to avoid redundant calculations.

## Approach
Dynamic programming can be implemented using two main techniques: **memoization** and **tabulation**.

### 1. Memoization
Memoization is a top-down approach where the problem is solved recursively, and the results of subproblems are stored in a data structure (usually a hash table or array) to avoid recomputation. When a subproblem is encountered, the algorithm first checks if the result is already computed.

#### Example: Fibonacci Sequence
The Fibonacci sequence can be computed using memoization as follows:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

### 2. Tabulation
Tabulation is a bottom-up approach where the problem is solved iteratively. A table (usually an array) is constructed to store the results of subproblems, and the final solution is built from these stored results.

#### Example: Fibonacci Sequence
The Fibonacci sequence can also be computed using tabulation:

```python
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
```

## Applications
Dynamic programming is widely used in various fields, including:

- **Operations Research**: For resource allocation and scheduling problems.
- **Computer Science**: In algorithms for string matching, graph theory, and optimization problems.
- **Economics**: For modeling dynamic systems and decision-making processes.
- **Bioinformatics**: In sequence alignment and other computational biology problems.

## Common Problems Solved with Dynamic Programming
1. **Fibonacci Sequence**: Efficient computation of Fibonacci numbers.
2. **Knapsack Problem**: Maximizing value with weight constraints.
3. **Longest Common Subsequence**: Finding the longest subsequence common to two sequences.
4. **Edit Distance**: Calculating the minimum number of operations required to transform one string into another.
5. **Matrix Chain Multiplication**: Optimizing the order of matrix multiplications.

## Complexity
The time and space complexity of dynamic programming algorithms can vary based on the specific problem and the approach used. Generally, dynamic programming reduces the time complexity from exponential to polynomial by avoiding redundant calculations.

## Conclusion
Dynamic programming is a powerful technique for solving optimization problems by leveraging the properties of optimal substructure and overlapping subproblems. Its applications span various domains, making it an essential tool in algorithm design and analysis.

[[memoization]] | [[tabulation]] | [[optimal substructure]] | [[overlapping subproblems]] | [[Fibonacci sequence]] | [[Knapsack problem]] | [[Longest Common Subsequence]] | [[Edit distance]]
