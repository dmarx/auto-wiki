
# [[Binomial Coefficient]]

## Overview
The [[Binomial Coefficient]], denoted as \( \binom{n}{k} \), is a fundamental concept in combinatorics that represents the number of ways to choose \( k \) elements from a set of \( n \) elements without regard to the order of selection. Binomial coefficients are widely used in various fields, including probability, statistics, and algebra.

## Definition
The binomial coefficient is defined mathematically as:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

where:
- \( n! \) (n factorial) is the product of all positive integers up to \( n \),
- \( k! \) is the factorial of \( k \),
- \( (n-k)! \) is the factorial of \( n-k \).

This formula is valid for \( n \geq 0 \) and \( 0 \leq k \leq n \). If \( k > n \), then \( \binom{n}{k} = 0 \).

### Example
For example, to calculate \( \binom{5}{2} \):

\[
\binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5 \times 4}{2 \times 1} = 10
\]

This result indicates that there are 10 ways to choose 2 elements from a set of 5.

## Properties
The binomial coefficient has several important properties:

### 1. Symmetry
The binomial coefficient exhibits symmetry, which can be expressed as:

\[
\binom{n}{k} = \binom{n}{n-k}
\]

This property reflects the fact that choosing \( k \) elements from \( n \) is equivalent to leaving out \( n-k \) elements.

### 2. Pascal's Identity
Pascal's identity relates binomial coefficients in a recursive manner:

\[
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
\]

This identity can be visualized using Pascal's triangle, where each entry is the sum of the two entries directly above it.

### 3. Sum of Binomial Coefficients
The sum of the binomial coefficients for a fixed \( n \) is given by:

\[
\sum_{k=0}^{n} \binom{n}{k} = 2^n
\]

This identity indicates that the total number of subsets of a set with \( n \) elements is \( 2^n \).

## Applications
1. **Combinatorial Counting**: Binomial coefficients are used to count combinations in various combinatorial problems, such as selecting teams or forming committees.
  
2. **Probability Theory**: In probability, binomial coefficients appear in the binomial distribution, which models the number of successes in a fixed number of independent Bernoulli trials.

3. **Algebra**: Binomial coefficients are integral to the [[Binomial Theorem]], which provides a formula for expanding powers of binomials:

\[
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k
\]

## Conclusion
The binomial coefficient is a crucial concept in combinatorics, providing a systematic way to count combinations and contributing to various mathematical theories and applications. Its properties and relationships with other mathematical constructs make it a foundational element in both pure and applied mathematics.

## References
- Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). *Concrete Mathematics: A Foundation for Computer Science*. Addison-Wesley.
- Wilf, H. S. (1994). *Generatingfunctionology*. Academic Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*. Wiley.

