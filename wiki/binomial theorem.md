
# Binomial Theorem

## Definition
The [[Binomial Theorem]] provides a formula for the expansion of powers of binomials. A binomial is an algebraic expression containing two terms, typically expressed in the form \( (a + b) \). The theorem states that for any non-negative integer \( n \):

\[
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
\]

where \( \binom{n}{k} \) is the [[binomial coefficient]], defined as:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

with \( n! \) (n factorial) being the product of all positive integers up to \( n \).

## Components of the Theorem

### Binomial Coefficient
The binomial coefficient \( \binom{n}{k} \) counts the number of ways to choose \( k \) elements from a set of \( n \) elements without regard to the order of selection. It can also be interpreted combinatorially as the number of distinct subsets of size \( k \) that can be formed from a set of size \( n \).

### Expansion Terms
In the expansion \( (a + b)^n \):
- Each term in the expansion is of the form \( \binom{n}{k} a^{n-k} b^k \).
- The exponent of \( a \) decreases from \( n \) to \( 0 \) as \( k \) increases from \( 0 \) to \( n \).
- The exponent of \( b \) increases from \( 0 \) to \( n \) as \( k \) increases.

### Example
For \( n = 3 \):
\[
(a + b)^3 = \binom{3}{0} a^3 b^0 + \binom{3}{1} a^2 b^1 + \binom{3}{2} a^1 b^2 + \binom{3}{3} a^0 b^3
\]
Calculating the coefficients:
\[
= 1 \cdot a^3 + 3 \cdot a^2 b + 3 \cdot a b^2 + 1 \cdot b^3 = a^3 + 3a^2b + 3ab^2 + b^3
\]

## Generalization

### Multinomial Theorem
The Binomial Theorem can be generalized to the [[Multinomial Theorem]], which describes the expansion of powers of sums of more than two terms. For any positive integer \( n \) and any set of variables \( x_1, x_2, \ldots, x_m \):

\[
(x_1 + x_2 + \ldots + x_m)^n = \sum_{k_1 + k_2 + \ldots + k_m = n} \frac{n!}{k_1! k_2! \ldots k_m!} x_1^{k_1} x_2^{k_2} \ldots x_m^{k_m}
\]

where the sum is taken over all non-negative integer combinations \( k_1, k_2, \ldots, k_m \) such that their sum equals \( n \).

## Applications
The Binomial Theorem has numerous applications in various fields, including:
- **Combinatorics**: Counting combinations and permutations.
- **Probability Theory**: Deriving distributions, such as the [[Binomial Distribution]], which models the number of successes in a fixed number of independent Bernoulli trials.
- **Algebra**: Simplifying polynomial expressions and solving equations.

## Conclusion
The Binomial Theorem is a fundamental result in algebra that facilitates the expansion of binomials raised to a power. Its implications extend into various mathematical disciplines, making it a crucial tool for both theoretical and applied mathematics.

[[Further Reading]]: Explore related topics such as [[Combinatorial Identities]], [[Pascal's Triangle]], and [[Generating Functions]] for deeper insights into the applications and extensions of the Binomial Theorem.
