
# Probability Theory

## Overview
Probability theory is a branch of mathematics that deals with the analysis of random phenomena. It provides a formal framework for quantifying uncertainty and making inferences based on incomplete information. Probability theory is foundational for various fields, including statistics, finance, machine learning, and scientific research.

## Fundamental Concepts

### Sample Space
The sample space \( S \) is the set of all possible outcomes of a random experiment. For example, when flipping a coin, the sample space is:

\[
S = \{ \text{Heads}, \text{Tails} \}
\]

### Events
An event \( A \) is a subset of the sample space. Events can be simple (containing a single outcome) or compound (containing multiple outcomes). The probability of an event \( A \) is denoted as \( P(A) \).

### Probability Measure
A probability measure is a function that assigns a probability to each event in a sample space, satisfying the following properties:

1. **Non-negativity**: \( P(A) \geq 0 \) for any event \( A \).
2. **Normalization**: \( P(S) = 1 \), meaning the probability of the entire sample space is 1.
3. **Additivity**: For any two mutually exclusive events \( A \) and \( B \):

\[
P(A \cup B) = P(A) + P(B)
\]

### Conditional Probability
The conditional probability of an event \( A \) given another event \( B \) is defined as:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]

provided that \( P(B) > 0 \). This concept is crucial for understanding dependencies between events.

### Independence
Two events \( A \) and \( B \) are said to be independent if the occurrence of one does not affect the probability of the other:

\[
P(A \cap B) = P(A) P(B)
\]

### Random Variables
A random variable \( X \) is a function that assigns a numerical value to each outcome in the sample space. Random variables can be classified into two types:

- **Discrete Random Variables**: Take on a countable number of values. The probability mass function (PMF) \( p(x) \) gives the probability that \( X \) takes the value \( x \).

- **Continuous Random Variables**: Take on an uncountable number of values. The probability density function (PDF) \( f(x) \) describes the likelihood of \( X \) taking a value in a given interval. The probability of \( X \) falling within an interval \( [a, b] \) is given by:

\[
P(a \leq X \leq b) = \int_a^b f(x) \, dx
\]

### Expectation and Variance
The expectation (or mean) of a random variable \( X \) is a measure of its central tendency, defined as:

\[
E[X] = \sum_{x} x \cdot p(x) \quad \text{(for discrete)} \quad \text{or} \quad E[X] = \int_{-\infty}^{\infty} x f(x) \, dx \quad \text{(for continuous)}
\]

The variance \( \text{Var}(X) \) measures the spread of the random variable around its mean:

\[
\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
\]

### Law of Large Numbers
The law of large numbers states that as the number of trials increases, the sample average of a random variable converges to the expected value:

\[
\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} X_i = E[X] \quad \text{(with probability 1)}
\]

### Central Limit Theorem
The central limit theorem states that the distribution of the sum (or average) of a large number of independent and identically distributed random variables approaches a normal distribution, regardless of the original distribution of the variables. Mathematically, if \( X_1, X_2, \ldots, X_n \) are i.i.d. random variables with mean \( \mu \) and variance \( \sigma^2 \), then:

\[
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty
\]

where \( \bar{X} \) is the sample mean and \( N(0, 1) \) is the standard normal distribution.

## Applications
Probability theory has a wide range of