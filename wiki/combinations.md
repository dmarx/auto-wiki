
# Combinations

## Definition
In combinatorial mathematics, a [[combination]] is a selection of items from a larger set, where the order of selection does not matter. Combinations are a fundamental concept in combinatorics, often used in probability, statistics, and various fields of mathematics.

## Mathematical Notation
The number of ways to choose \( k \) elements from a set of \( n \) elements is denoted as \( \binom{n}{k} \), known as the binomial coefficient. It is defined mathematically as:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

where:
- \( n! \) (n factorial) is the product of all positive integers up to \( n \).
- \( k! \) is the factorial of \( k \).
- \( (n-k)! \) is the factorial of the difference between \( n \) and \( k \).

### Example
To illustrate, consider a set \( S = \{1, 2, 3, 4\} \) and the task of selecting 2 elements from this set. The combinations can be calculated as follows:

\[
\binom{4}{2} = \frac{4!}{2!(4-2)!} = \frac{4 \times 3}{2 \times 1} = 6
\]

The possible combinations are:
- \( \{1, 2\} \)
- \( \{1, 3\} \)
- \( \{1, 4\} \)
- \( \{2, 3\} \)
- \( \{2, 4\} \)
- \( \{3, 4\} \)

## Properties of Combinations

### Symmetry
The binomial coefficient exhibits symmetry, which can be expressed as:
\[
\binom{n}{k} = \binom{n}{n-k}
\]
This property indicates that choosing \( k \) elements from \( n \) is equivalent to leaving out \( n-k \) elements.

### Pascal's Triangle
The values of \( \binom{n}{k} \) can be arranged in a triangular array known as [[Pascal's Triangle]], where each entry is the sum of the two entries directly above it:
\[
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
\]

### Combinations with Repetition
When repetitions of elements are allowed, the number of ways to choose \( k \) elements from \( n \) types of items is given by the formula:
\[
\binom{n+k-1}{k}
\]
This is often referred to as the "stars and bars" theorem in combinatorics.

## Applications
Combinations are widely used in various fields, including:
- **Probability Theory**: Calculating the likelihood of events where the order of outcomes does not matter.
- **Statistics**: Designing experiments and sampling methods.
- **Computer Science**: Algorithms for generating combinations and solving combinatorial problems.

## Conclusion
Combinations are a crucial concept in combinatorial mathematics, providing a framework for understanding how to select items from a set without regard to order. Their properties and applications extend across multiple disciplines, making them essential for both theoretical and applied mathematics.

[[Further Reading]]: Explore related topics such as [[Permutations]], [[Binomial Theorem]], and [[Combinatorial Optimization]] for deeper insights into the principles and applications of combinations.
