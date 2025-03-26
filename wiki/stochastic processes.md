
# Stochastic Processes

## Overview
A [[stochastic process]] is a mathematical object that describes a collection of random variables indexed by time or space. Stochastic processes are used to model systems that evolve over time in a probabilistic manner, making them essential in fields such as [[finance]], [[queueing theory]], [[statistical mechanics]], and [[machine learning]].

## Mathematical Definition

### Formal Definition
A stochastic process can be formally defined as a family of random variables \( \{X(t) : t \in T\} \), where \( T \) is an index set (often representing time) and each \( X(t) \) takes values in a measurable space \( S \). The collection of random variables is typically indexed by time \( t \) in continuous or discrete formats.

### Types of Stochastic Processes
Stochastic processes can be classified based on various criteria:

1. **Discrete vs. Continuous Time**:
   - **Discrete Time**: The index set \( T \) is a countable set, e.g., \( T = \{0, 1, 2, \ldots\} \).
   - **Continuous Time**: The index set \( T \) is an interval of real numbers, e.g., \( T = [0, \infty) \).

2. **Discrete vs. Continuous State Space**:
   - **Discrete State Space**: The values of \( X(t) \) take on a countable set of values, e.g., \( S = \{0, 1, 2, \ldots\} \).
   - **Continuous State Space**: The values of \( X(t) \) can take on any value in a continuum, e.g., \( S = \mathbb{R} \).

3. **Markov vs. Non-Markov Processes**:
   - **Markov Process**: The future state depends only on the present state and not on the past states, formally expressed as:
     \[
     P(X(t+s) = x | X(t) = y, X(u) = z \text{ for } u < t) = P(X(t+s) = x | X(t) = y)
     \]
   - **Non-Markov Process**: The future state depends on the entire history of the process.

## Key Examples

### Markov Chains
A [[Markov chain]] is a discrete-time stochastic process with a finite or countable state space that satisfies the Markov property. The transition probabilities are defined as:
\[
P(X_{n+1} = j | X_n = i) = p_{ij}
\]
where \( p_{ij} \) is the probability of transitioning from state \( i \) to state \( j \).

### Brownian Motion
[[Brownian motion]], or Wiener process, is a continuous-time stochastic process that serves as a mathematical model for random motion. It is characterized by:
- \( B(0) = 0 \)
- Independent increments: \( B(t) - B(s) \) is independent of \( B(u) \) for \( u \leq s \)
- Normally distributed increments: \( B(t) - B(s) \sim \mathcal{N}(0, t-s) \)

### Poisson Process
A [[Poisson process]] is a stochastic process that models a series of events occurring randomly over time. It is characterized by:
- The number of events in a time interval follows a Poisson distribution.
- The increments are independent and stationary.

## Applications

### Finance
Stochastic processes are widely used in finance to model asset prices, interest rates, and risk. The Black-Scholes model, for instance, uses geometric Brownian motion to describe the dynamics of stock prices.

### Queueing Theory
In queueing theory, stochastic processes model the arrival of customers and the service times in systems such as telecommunications and computer networks. The analysis often involves Markovian models, such as the M/M/1 queue.

### Machine Learning
In machine learning, stochastic processes underpin various algorithms, including reinforcement learning, where agents learn to make decisions based on stochastic environments.

## Conclusion
Stochastic processes provide a robust framework for modeling and analyzing systems that exhibit randomness over time. Their versatility and applicability across diverse fields underscore their importance in both theoretical and applied contexts.

## References
- [[Markov Chains]]
- [[Brownian Motion]]
- [[Poisson Process]]
- [[Queueing Theory]]
