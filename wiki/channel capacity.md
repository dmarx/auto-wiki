
# Channel Capacity

## Overview
Channel capacity is a fundamental concept in information theory that quantifies the maximum rate at which information can be reliably transmitted over a communication channel. It is defined as the highest achievable data rate at which the probability of error in transmission approaches zero as the length of the message increases. The concept was introduced by [[Claude Shannon]] in his seminal 1948 paper, "A Mathematical Theory of Communication."

## Mathematical Definition
The channel capacity \( C \) of a discrete memoryless channel (DMC) can be expressed mathematically as:
\[
C = \max_{P(X)} I(X; Y)
\]
where:
- \( I(X; Y) \) is the [[mutual information]] between the input \( X \) and the output \( Y \) of the channel.
- \( P(X) \) is the probability distribution of the input \( X \).

### Mutual Information
The mutual information \( I(X; Y) \) is defined as:
\[
I(X; Y) = H(X) - H(X | Y)
\]
where:
- \( H(X) \) is the entropy of the input \( X \), representing the average uncertainty in the input.
- \( H(X | Y) \) is the conditional entropy of \( X \) given \( Y \), representing the remaining uncertainty about \( X \) after observing \( Y \).

### Capacity of Specific Channels
1. **Binary Symmetric Channel (BSC)**: For a BSC with crossover probability \( p \), the channel capacity is given by:
   \[
   C = 1 - H(p)
   \]
   where \( H(p) = -p \log_2 p - (1-p) \log_2 (1-p) \) is the binary entropy function.

2. **Additive White Gaussian Noise (AWGN) Channel**: For an AWGN channel with bandwidth \( B \) and signal-to-noise ratio (SNR) \( \gamma \), the channel capacity is expressed as:
   \[
   C = B \log_2(1 + \gamma)
   \]

## Properties of Channel Capacity
1. **Non-negativity**: The channel capacity is always non-negative, meaning that a channel can transmit at least zero bits of information.
2. **Additivity**: For independent channels, the capacity of the combined channel is the sum of the individual capacities.
3. **Dependence on Input Distribution**: The capacity can vary depending on the input distribution \( P(X) \). The optimal input distribution maximizes the mutual information.

## Applications
Channel capacity has significant implications in various fields, including:
- **Telecommunications**: Designing efficient coding schemes to approach the theoretical limits of data transmission.
- **Data Compression**: Understanding the limits of lossless and lossy compression techniques.
- **Network Theory**: Analyzing the performance of communication networks and optimizing data flow.

## Shannon's Theorems
Shannon's theorems provide foundational results regarding channel capacity:
1. **Shannon's Noisy Channel Coding Theorem**: States that for any rate \( R < C \), there exists a coding scheme that allows for reliable communication with an arbitrarily low probability of error.
2. **Shannon's Source Coding Theorem**: Establishes the limits of data compression, indicating that the average length of the encoded message can be made arbitrarily close to the entropy of the source.

## Conclusion
Channel capacity is a critical concept in information theory that defines the limits of reliable communication over a channel. Understanding channel capacity enables the design of efficient communication systems and informs the development of coding strategies that approach these theoretical limits.
