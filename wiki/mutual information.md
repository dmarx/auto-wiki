
# Mutual Information

## Overview
[[Mutual Information]] (MI) is a fundamental concept in [[Information Theory]] that quantifies the amount of information obtained about one random variable through another random variable. It measures the reduction in uncertainty of one variable given knowledge of the other, thus capturing the degree of dependence between the two variables.

## Definition
For two discrete random variables \( X \) and \( Y \) with joint probability distribution \( P(X, Y) \) and marginal distributions \( P(X) \) and \( P(Y) \), the mutual information \( I(X; Y) \) is defined as:

\[
I(X; Y) = H(X) + H(Y) - H(X, Y)
\]

where:
- \( H(X) \) is the entropy of \( X \),
- \( H(Y) \) is the entropy of \( Y \),
- \( H(X, Y) \) is the joint entropy of \( X \) and \( Y \).

### Alternative Formulation
Mutual information can also be expressed in terms of the conditional entropy \( H(Y|X) \):

\[
I(X; Y) = H(Y) - H(Y|X)
\]

This formulation emphasizes that mutual information quantifies the amount of uncertainty in \( Y \) that is resolved by knowing \( X \).

## Properties

### 1. Non-negativity
Mutual information is always non-negative:

\[
I(X; Y) \geq 0
\]

This property indicates that knowing \( X \) cannot increase the uncertainty about \( Y \).

### 2. Symmetry
Mutual information is symmetric:

\[
I(X; Y) = I(Y; X)
\]

This means that the amount of information gained about \( X \) from \( Y \) is equal to the amount of information gained about \( Y \) from \( X \).

### 3. Zero Mutual Information
If \( X \) and \( Y \) are independent, then:

\[
I(X; Y) = 0
\]

This indicates that knowing \( X \) provides no information about \( Y \) and vice versa.

## Calculation Example
Consider two binary random variables \( X \) and \( Y \) with the following joint probability distribution:

| \( X \backslash Y \) | 0   | 1   |
|-----------------------|-----|-----|
| 0                     | 0.1 | 0.4 |
| 1                     | 0.2 | 0.3 |

### Step 1: Calculate Marginal Distributions
- \( P(X=0) = 0.1 + 0.4 = 0.5 \)
- \( P(X=1) = 0.2 + 0.3 = 0.5 \)
- \( P(Y=0) = 0.1 + 0.2 = 0.3 \)
- \( P(Y=1) = 0.4 + 0.3 = 0.7 \)

### Step 2: Calculate Entropies
- **Entropy of \( X \)**:
\[
H(X) = -\left( P(X=0) \log_2 P(X=0) + P(X=1) \log_2 P(X=1) \right) = -\left( 0.5 \log_2 0.5 + 0.5 \log_2 0.5 \right) = 1
\]

- **Entropy of \( Y \)**:
\[
H(Y) = -\left( P(Y=0) \log_2 P(Y=0) + P(Y=1) \log_2 P(Y=1) \right) = -\left( 0.3 \log_2 0.3 + 0.7 \log_2 0.7 \right) \approx 0.881
\]

- **Joint Entropy \( H(X, Y) \)**:
\[
H(X, Y) = -\sum_{x} \sum_{y} P(x, y) \log_2 P(x, y) = -\left( 0.1 \log_2 0.1 + 0.4 \log_2 0.4 + 0.2 \log_2 0.2 + 0.3 \log_2 0.3 \right) \approx 1.846
\]

### Step 3: Calculate Mutual Information
\[
I(X; Y) = H(X) + H(Y) - H(X, Y) = 1 + 0.881 - 1.846 \approx 0.035
\]

## Applications
Mutual information is widely used in various fields, including:
- **Machine Learning**: For feature selection and