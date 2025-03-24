
# Combination

## Definition
A [[combination]] is a selection of items from a larger set, where the order of selection does not matter. Combinations are a fundamental concept in [[combinatorics]], which is the branch of mathematics dealing with counting, arrangement, and combination of objects.

## Mathematical Representation
The number of ways to choose \( k \) elements from a set of \( n \) distinct elements is denoted as \( \binom{n}{k} \), known as the binomial coefficient. It is defined mathematically as:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

where \( n! \) (n factorial) is the product of all positive integers up to \( n \):

\[
n! = n \times (n-1) \times (n-2) \times \ldots \times 2 \times 1
\]

## Properties
1. **Symmetry**: The binomial coefficient exhibits symmetry, meaning:
   \[
   \binom{n}{k} = \binom{n}{n-k}
   \]
   This property indicates that choosing \( k \) elements from \( n \) is equivalent to leaving out \( n-k \) elements.

2. **Sum of Combinations**: The sum of combinations for a fixed \( n \) across all possible \( k \) values is given by:
   \[
   \sum_{k=0}^{n} \binom{n}{k} = 2^n
   \]
   This identity reflects the total number of subsets of a set with \( n \) elements.

3. **Combination of Combinations**: The number of ways to choose \( k \) combinations from \( n \) combinations is given by:
   \[
   \binom{n}{k} \cdot \binom{m}{r} = \frac{n!}{k!(n-k)!} \cdot \frac{m!}{r!(m-r)!}
   \]
   where \( m \) is the total number of combinations available.

## Applications
Combinations are widely used in various fields, including:

- **Statistics**: In hypothesis testing and confidence intervals, combinations help determine sample sizes and selection methods.
- **Probability Theory**: Combinations are essential in calculating probabilities of events where the order does not matter.
- **Computer Science**: Algorithms for generating combinations are used in optimization problems, cryptography, and data analysis.

## Symbolic Notation
Let \( C(n, k) \) denote the number of combinations of \( n \) items taken \( k \) at a time. Then:

\[
C(n, k) = \binom{n}{k}
\]

for \( k = 0, 1, \ldots, n \).

## Related Concepts
- [[Permutations]]: Unlike combinations, permutations consider the order of selection, leading to different counting methods.
- [[Binomial Theorem]]: The theorem that describes the algebraic expansion of powers of a binomial, which is closely related to combinations.
- [[Stirling Numbers]]: These numbers count the ways to partition a set of \( n \) objects into \( k \) non-empty subsets, providing a deeper combinatorial context.

## Conclusion
Combinations are a crucial concept in combinatorial mathematics, providing a framework for understanding selections and arrangements where order is irrelevant. Mastery of combinations is essential for advanced studies in statistics, probability, and various applications in science and engineering.
