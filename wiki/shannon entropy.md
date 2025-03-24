
# Shannon Entropy

## Definition
Shannon entropy, denoted as \( H(X) \), is a measure of the uncertainty associated with a random variable \( X \). It quantifies the average amount of information produced by a stochastic source of data. The concept was introduced by Claude Shannon in his seminal 1948 paper, "A Mathematical Theory of Communication."

## Mathematical Formulation
For a discrete random variable \( X \) that can take on \( n \) possible values \( x_1, x_2, \ldots, x_n \) with corresponding probabilities \( p(x_1), p(x_2), \ldots, p(x_n) \), the Shannon entropy is defined as:

\[
H(X) = -\sum_{i=1}^{n} p(x_i) \log_b p(x_i)
\]

where:
- \( H(X) \) is the entropy of the random variable \( X \),
- \( p(x_i) \) is the probability of occurrence of the value \( x_i \),
- \( b \) is the base of the logarithm, which determines the unit of entropy (base 2 for bits, base \( e \) for nats, and base 10 for dits).

### Properties
1. **Non-negativity**: \( H(X) \geq 0 \) for all random variables \( X \).
2. **Maximum Entropy**: The entropy is maximized when all outcomes are equally likely, i.e., \( p(x_i) = \frac{1}{n} \) for all \( i \). In this case, \( H(X) = \log_b n \).
3. **Additivity**: For two independent random variables \( X \) and \( Y \), the joint entropy satisfies:
   \[
   H(X, Y) = H(X) + H(Y)
   \]
4. **Chain Rule**: The entropy of a joint distribution can be expressed in terms of conditional entropies:
   \[
   H(X, Y) = H(X) + H(Y | X)
   \]

## Applications
Shannon entropy has profound implications in various fields, including:
- **Information Theory**: It serves as a foundational concept for quantifying information content and data compression.
- **Machine Learning**: Used in algorithms such as decision trees, where it helps in determining the best feature to split data.
- **Cryptography**: Entropy measures the unpredictability of keys and the security of cryptographic systems.

## Related Concepts
- **Conditional Entropy**: The entropy of a random variable given the value of another variable, denoted as \( H(Y | X) \).
- **Mutual Information**: A measure of the amount of information that one random variable contains about another, defined as:
  \[
  I(X; Y) = H(X) + H(Y) - H(X, Y)
  \]
- **Kullback-Leibler Divergence**: A measure of how one probability distribution diverges from a second expected probability distribution, defined as:
  \[
  D_{KL}(P || Q) = \sum_{i} p(x_i) \log \frac{p(x_i)}{q(x_i)}
  \]

## Conclusion
Shannon entropy is a cornerstone of information theory, providing a quantitative measure of uncertainty and information content. Its applications span across various domains, making it a critical concept for researchers in fields such as data science, machine learning, and cryptography.

[[Information Theory]] | [[Mutual Information]] | [[Kullback-Leibler Divergence]] | [[Conditional Entropy]]
