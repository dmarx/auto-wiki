
# Permutations

## Definition
A [[permutation]] of a set is a specific arrangement of its elements. For a finite set of \( n \) distinct elements, a permutation is any of the \( n! \) (factorial of \( n \)) possible arrangements. The factorial function is defined as:

\[
n! = n \times (n-1) \times (n-2) \times \ldots \times 2 \times 1
\]

## Notation
Permutations can be denoted in various ways, including:

1. **Cycle Notation**: A permutation can be expressed as a product of disjoint cycles. For example, the permutation \( (1, 3, 2) \) indicates that 1 goes to 3, 3 goes to 2, and 2 goes back to 1.

2. **Two-Line Notation**: A permutation can also be represented in two lines, where the first line lists the original elements and the second line lists the images of these elements under the permutation. For example, the permutation \( \sigma \) of the set \( \{1, 2, 3\} \) can be written as:

\[
\sigma = \begin{pmatrix}
1 & 2 & 3 \\
3 & 1 & 2
\end{pmatrix}
\]

## Properties
- **Order of a Permutation**: The order of a permutation is the smallest positive integer \( k \) such that applying the permutation \( k \) times results in the identity permutation. 

- **Even and Odd Permutations**: A permutation is classified as even if it can be expressed as a product of an even number of transpositions (two-element swaps), and odd if it can be expressed as a product of an odd number of transpositions. The parity of a permutation is an important concept in [[group theory]].

## Applications
Permutations are fundamental in various fields, including:

- **Combinatorics**: Counting arrangements and selections.
- **Cryptography**: Permutations are used in various encryption algorithms.
- **Computer Science**: Algorithms for sorting and searching often utilize permutations.

## Mathematical Formalism
Let \( S = \{1, 2, \ldots, n\} \) be a set of \( n \) elements. A permutation \( \sigma \) of \( S \) can be defined as a bijective function \( \sigma: S \to S \). The set of all permutations of \( S \) is denoted as \( S_n \), and it forms a group under the operation of composition, known as the symmetric group.

### Group Properties
The symmetric group \( S_n \) has the following properties:

- **Closure**: For any two permutations \( \sigma, \tau \in S_n \), the composition \( \sigma \circ \tau \) is also in \( S_n \).
- **Associativity**: Composition of permutations is associative.
- **Identity Element**: The identity permutation \( e \) such that \( e(x) = x \) for all \( x \in S \) exists in \( S_n \).
- **Inverses**: For every permutation \( \sigma \in S_n \), there exists an inverse permutation \( \sigma^{-1} \) such that \( \sigma \circ \sigma^{-1} = e \).

## Related Concepts
- [[Combinations]]: Unlike permutations, combinations refer to selections of elements without regard to the order.
- [[Factorial]]: The mathematical function that counts the number of ways to arrange \( n \) distinct objects.
- [[Stirling Numbers]]: These numbers count the ways to partition a set of \( n \) objects into \( k \) non-empty subsets, which relates to permutations in combinatorial contexts.

## Conclusion
Permutations are a foundational concept in mathematics, particularly in combinatorics and group theory. Understanding their properties and applications is crucial for advanced studies in these areas.
