
# Relative Entropy

## Definition
**Relative entropy**, also known as **Kullback-Leibler divergence (KL divergence)**, is a measure of how one probability distribution diverges from a second, expected probability distribution. It quantifies the information lost when one distribution is used to approximate another. Relative entropy is widely used in statistics, information theory, and machine learning.

## Mathematical Formulation
Given two probability distributions \( P \) and \( Q \) defined over the same probability space, the relative entropy \( D_{KL}(P \| Q) \) is defined as:

\[
D_{KL}(P \| Q) = \sum_{x} P(x) \log \frac{P(x)}{Q(x)}
\]

for discrete distributions, or

\[
D_{KL}(P \| Q) = \int_{-\infty}^{\infty} p(x) \log \frac{p(x)}{q(x)} \, dx
\]

for continuous distributions, where:
- \( P \) is the true distribution (often referred to as the "target" distribution),
- \( Q \) is the approximating distribution (often referred to as the "model" distribution),
- \( p(x) \) and \( q(x) \) are the probability density functions of \( P \) and \( Q \), respectively.

### Properties
1. **Non-negativity**: \( D_{KL}(P \| Q) \geq 0 \) for all \( P \) and \( Q \). The divergence is zero if and only if \( P = Q \) almost everywhere.
2. **Asymmetry**: \( D_{KL}(P \| Q) \neq D_{KL}(Q \| P) \). This means that the measure is not symmetric; the divergence from \( P \) to \( Q \) is not necessarily the same as from \( Q \) to \( P \).
3. **Information Gain**: Relative entropy can be interpreted as the expected log difference between the probabilities assigned by the two distributions, providing a measure of the information gained when moving from \( Q \) to \( P \).

## Applications
- **Machine Learning**: KL divergence is commonly used in variational inference, where it measures the difference between the true posterior distribution and an approximate distribution.
- **Information Theory**: It quantifies the inefficiency of assuming that the distribution is \( Q \) when the true distribution is \( P \).
- **Statistics**: Relative entropy is used in model selection criteria, such as the Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC).

## Relation to Other Concepts
- **Cross-Entropy**: The cross-entropy between two distributions \( P \) and \( Q \) is defined as:

\[
H(P, Q) = -\sum_{x} P(x) \log Q(x)
\]

The relationship between cross-entropy and KL divergence is given by:

\[
D_{KL}(P \| Q) = H(P, Q) - H(P)
\]

where \( H(P) \) is the entropy of the distribution \( P \).

- **Entropy**: The entropy \( H(P) \) of a distribution \( P \) is defined as:

\[
H(P) = -\sum_{x} P(x) \log P(x)
\]

Entropy measures the uncertainty inherent in the distribution \( P \).

## Example
Consider two discrete probability distributions:
- \( P = [0.9, 0.1] \)
- \( Q = [0.8, 0.2] \)

The KL divergence can be calculated as follows:

\[
D_{KL}(P \| Q) = 0.9 \log \frac{0.9}{0.8} + 0.1 \log \frac{0.1}{0.2}
\]

Calculating this gives a measure of how much information is lost when using \( Q \) to approximate \( P \).

## Conclusion
Relative entropy is a crucial concept in various fields, providing insights into the efficiency of probabilistic models and the information content of distributions. Its properties and applications make it a fundamental tool in statistical analysis and machine learning.

## Related Concepts
- [[Kullback-Leibler Divergence]]
- [[Cross-Entropy]]
- [[Entropy]]
- [[Information Theory]]
- [[Variational Inference]]
- [[Model Selection]]
