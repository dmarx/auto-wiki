
# Knapsack Problem

## Definition
The [[knapsack problem]] is a classic optimization problem in combinatorial optimization. It involves selecting a subset of items, each with a given weight and value, to maximize the total value without exceeding a specified weight capacity. The problem can be categorized into several variants, including the 0/1 knapsack problem, the fractional knapsack problem, and the unbounded knapsack problem.

## Mathematical Formulation
Let \( n \) be the number of items, each item \( i \) has a weight \( w_i \) and a value \( v_i \). The goal is to maximize the total value \( V \) of the selected items while ensuring that the total weight \( W \) does not exceed the capacity \( C \) of the knapsack.

### 0/1 Knapsack Problem
In the 0/1 knapsack problem, each item can either be included in the knapsack or excluded (i.e., no fractional items). The problem can be formulated as follows:

\[
\text{Maximize } V = \sum_{i=1}^{n} v_i x_i
\]

subject to:

\[
\sum_{i=1}^{n} w_i x_i \leq C
\]

where \( x_i \in \{0, 1\} \) indicates whether item \( i \) is included in the knapsack.

### Fractional Knapsack Problem
In the fractional knapsack problem, items can be broken into smaller parts, allowing for fractional inclusion. The objective remains the same:

\[
\text{Maximize } V = \sum_{i=1}^{n} v_i x_i
\]

subject to:

\[
\sum_{i=1}^{n} w_i x_i \leq C
\]

where \( x_i \) can take any value in the range \( [0, 1] \).

### Unbounded Knapsack Problem
In the unbounded knapsack problem, there is no limit on the number of copies of each item that can be included. The formulation is similar to the 0/1 knapsack problem but allows for \( x_i \) to be any non-negative integer.

## Algorithms
Several algorithms can be employed to solve the knapsack problem, depending on the variant.

### 1. Dynamic Programming Approach (0/1 Knapsack)
The dynamic programming approach is commonly used for the 0/1 knapsack problem. We define a matrix \( K \) where \( K[i][j] \) represents the maximum value that can be attained with a weight limit \( j \) using the first \( i \) items.

#### Steps:
1. Initialize \( K[0][j] = 0 \) for all \( j \) (no items).
2. For each item \( i \) from 1 to \( n \):
   - For each weight \( j \) from 0 to \( C \):
     - If \( w_i \leq j \):
       \[
       K[i][j] = \max(K[i-1][j], K[i-1][j-w_i] + v_i)
       \]
     - Otherwise:
       \[
       K[i][j] = K[i-1][j]
       \]

The time complexity of this approach is \( O(nC) \), and the space complexity can be reduced to \( O(C) \) using a one-dimensional array.

### 2. Greedy Approach (Fractional Knapsack)
The greedy algorithm is suitable for the fractional knapsack problem. The items are sorted based on their value-to-weight ratio \( \frac{v_i}{w_i} \) in descending order. The algorithm iteratively adds items to the knapsack until the capacity is reached.

#### Steps:
1. Calculate the value-to-weight ratio for each item.
2. Sort items by this ratio.
3. Initialize total value \( V = 0 \) and total weight \( W = 0 \).
4. For each item:
   - If adding the entire item does not exceed capacity, add it completely.
   - If it exceeds, add the fractional part that fits.

The time complexity of this approach is \( O(n \log n) \) due to the sorting step.

## Applications
The knapsack problem has numerous applications in various fields, including:

- **Resource Allocation**: Optimizing the allocation of limited resources in finance and operations.
- **Cargo Loading**: Determining the optimal loading of cargo in transportation.
- **Budget Management**: Selecting projects or investments within a budget constraint.

## Conclusion
The knapsack problem is a fundamental problem in optimization with significant implications in various domains. Understanding its variants and the appropriate algorithms for solving them is crucial for effective decision-making in resource allocation and optimization tasks.

[[dynamic programming]] | [[greedy algorithms]] | [[combinatorial optimization]] | [[0/1 knapsack problem]]