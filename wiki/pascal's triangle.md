
# Pascal's Triangle

## Definition
[[Pascal's Triangle]] is a triangular array of the binomial coefficients, which arise in the expansion of a binomial expression. Each entry in the triangle is the sum of the two entries directly above it. The \( n \)-th row of Pascal's Triangle corresponds to the coefficients of the expansion of \( (a + b)^n \).

## Construction
The triangle is constructed as follows:

1. The topmost row (row 0) contains a single element, which is 1.
2. Each subsequent row starts and ends with 1.
3. Each interior element is calculated as the sum of the two elements directly above it.

The first few rows of Pascal's Triangle are:

\[
\begin{array}{cccccc}
 & & & 1 & & \\
 & & 1 & & 1 & \\
 & 1 & & 2 & & 1 \\
1 & & 3 & & 3 & & 1 \\
\end{array}
\]

## Mathematical Representation
The \( n \)-th row of Pascal's Triangle can be represented using binomial coefficients, denoted as \( \binom{n}{k} \), where \( k \) is the index of the element in the row. The binomial coefficient is defined as:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

for \( k = 0, 1, 2, \ldots, n \).

## Properties
1. **Symmetry**: The triangle is symmetric, meaning \( \binom{n}{k} = \binom{n}{n-k} \).
2. **Sum of Rows**: The sum of the elements in the \( n \)-th row is \( 2^n \):
   \[
   \sum_{k=0}^{n} \binom{n}{k} = 2^n
   \]
3. **Hockey Stick Identity**: The sum of the elements in a diagonal line of the triangle gives another binomial coefficient:
   \[
   \sum_{i=r}^{n} \binom{i}{r} = \binom{n+1}{r+1}
   \]
4. **Fibonacci Sequence**: The Fibonacci numbers can be found by summing the appropriate diagonals of Pascal's Triangle.

## Applications
Pascal's Triangle has numerous applications in various fields:

- **Combinatorics**: It is used to calculate combinations and probabilities.
- **Algebra**: It aids in the expansion of binomial expressions.
- **Probability Theory**: It is used in calculating probabilities in binomial distributions.
- **Computer Science**: Algorithms for combinatorial problems often utilize Pascal's Triangle.

## Symbolic Notation
Let \( T(n, k) \) denote the entry in the \( n \)-th row and \( k \)-th column of Pascal's Triangle. Then:

\[
T(n, k) = \binom{n}{k}
\]

for \( k = 0, 1, \ldots, n \).

## Related Concepts
- [[Binomial Theorem]]: The theorem that describes the algebraic expansion of powers of a binomial.
- [[Combinatorial Identities]]: Various identities that can be derived from the properties of binomial coefficients.
- [[Fibonacci Numbers]]: A sequence of numbers where each number is the sum of the two preceding ones, which can be related to the sums of diagonals in Pascal's Triangle.

## Conclusion
Pascal's Triangle is a fundamental structure in mathematics, particularly in combinatorics and algebra. Its properties and applications extend across various domains, making it a vital tool for mathematical analysis and problem-solving.
