
# Information Theory

## Overview
[[Information Theory]] is a mathematical framework for quantifying the transmission, processing, and storage of information. It was founded by [[Claude Shannon]] in his seminal 1948 paper "A Mathematical Theory of Communication." The field has profound implications across various domains, including telecommunications, data compression, cryptography, and machine learning.

## Key Concepts

### 1. Information Content
The fundamental unit of information is the [[bit]], which represents the amount of information required to make a binary decision (e.g., yes/no, true/false). The information content \( I(x) \) of an event \( x \) with probability \( P(x) \) is defined as:

\[
I(x) = -\log_2 P(x)
\]

This formulation indicates that less probable events carry more information.

### 2. Entropy
[[Entropy]] is a measure of the uncertainty or randomness in a random variable. For a discrete random variable \( X \) with possible outcomes \( x_1, x_2, \ldots, x_n \) and corresponding probabilities \( P(x_1), P(x_2), \ldots, P(x_n) \), the entropy \( H(X) \) is defined as:

\[
H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)
\]

Entropy quantifies the average amount of information produced by a stochastic source of data.

### 3. Joint Entropy
The joint entropy \( H(X, Y) \) of two random variables \( X \) and \( Y \) is defined as:

\[
H(X, Y) = -\sum_{x \in X} \sum_{y \in Y} P(x, y) \log_2 P(x, y)
\]

This measures the total uncertainty associated with the pair of random variables.

### 4. Conditional Entropy
The conditional entropy \( H(Y|X) \) quantifies the amount of uncertainty remaining about \( Y \) given that \( X \) is known:

\[
H(Y|X) = H(X, Y) - H(X)
\]

### 5. Mutual Information
[[Mutual Information]] \( I(X; Y) \) measures the amount of information that knowing one of the variables provides about the other. It is defined as:

\[
I(X; Y) = H(X) + H(Y) - H(X, Y)
\]

Mutual information is symmetric, meaning \( I(X; Y) = I(Y; X) \).

### 6. Kullback-Leibler Divergence
The [[Kullback-Leibler Divergence]] (or relative entropy) \( D_{KL}(P || Q) \) measures how one probability distribution \( P \) diverges from a second, expected probability distribution \( Q \):

\[
D_{KL}(P || Q) = \sum_{x} P(x) \log \frac{P(x)}{Q(x)}
\]

This quantity is non-negative and is zero if and only if \( P \) and \( Q \) are identical.

## Applications

### 1. Data Compression
Information theory provides the theoretical foundation for data compression algorithms, such as [[Huffman coding]] and [[Shannon-Fano coding]], which aim to reduce the number of bits needed to represent data without loss of information.

### 2. Channel Capacity
The concept of [[Channel Capacity]] \( C \) quantifies the maximum rate at which information can be reliably transmitted over a communication channel. According to Shannon's theorem, the capacity of a noisy channel is given by:

\[
C = B \log_2(1 + \frac{S}{N})
\]

where \( B \) is the bandwidth of the channel, \( S \) is the average signal power, and \( N \) is the average noise power.

### 3. Machine Learning
In machine learning, information theory is used to evaluate model performance, feature selection, and the complexity of models. Metrics such as [[cross-entropy loss]] are derived from the principles of information theory.

## Conclusion
Information theory provides a robust mathematical framework for understanding and quantifying information in various contexts. Its principles are foundational to modern communication systems, data analysis, and machine learning methodologies.

## References
- Shannon, C. E. (1948). "A Mathematical Theory of Communication." Bell System Technical Journal.
- Cover, T. M., & Thomas, J. A. (2006). "Elements of Information Theory." Wiley-Interscience.
