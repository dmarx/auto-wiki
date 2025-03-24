
# Evolutionarily Stable Strategy (ESS)

## Definition
An Evolutionarily Stable Strategy (ESS) is a strategy that, if adopted by a population, cannot be invaded by any alternative strategy that is initially rare. The concept is a fundamental component of [[evolutionary game theory]], which applies game-theoretic principles to biological contexts, particularly in the study of animal behavior and evolutionary dynamics.

## Key Concepts

### 1. **Game Theory Basics**
In the context of game theory, players (or organisms) choose strategies to maximize their payoffs. The payoff can represent reproductive success, survival, or any other fitness measure. The strategies can be pure (a single action) or mixed (a probability distribution over actions).

### 2. **Fitness Payoff Matrix**
The interactions between strategies can be represented using a payoff matrix. For two strategies \( A \) and \( B \), the matrix can be structured as follows:

\[
\begin{array}{c|c|c}
 & A & B \\
\hline
A & P(A, A) & P(A, B) \\
\hline
B & P(B, A) & P(B, B) \\
\end{array}
\]

where \( P(X, Y) \) denotes the payoff received by strategy \( X \) when interacting with strategy \( Y \).

### 3. **ESS Conditions**
A strategy \( S \) is considered an ESS if it satisfies the following conditions:

1. **Condition 1**: If \( S \) is a best response against itself, then any mutant strategy \( T \) must not perform better than \( S \) when playing against \( S \):
   \[
   P(S, S) \geq P(T, S)
   \]

2. **Condition 2**: If \( S \) and \( T \) yield the same payoff when playing against \( S \), then \( S \) must perform better against \( T \):
   \[
   P(S, S) = P(T, S) \implies P(S, T) > P(T, T)
   \]

These conditions ensure that the strategy \( S \) is robust against invasions by alternative strategies.

### 4. **Example: Hawk-Dove Game**
The Hawk-Dove game is a classic example used to illustrate the concept of ESS. In this game, two strategies are considered:
- **Hawk**: Aggressive strategy that fights for resources.
- **Dove**: Non-aggressive strategy that shares resources.

The payoff matrix for the Hawk-Dove game can be represented as:

\[
\begin{array}{c|c|c}
 & \text{Hawk} & \text{Dove} \\
\hline
\text{Hawk} & \frac{V}{2} - C & V \\
\hline
\text{Dove} & 0 & \frac{V}{2} \\
\end{array}
\]

where \( V \) is the value of the resource and \( C \) is the cost of injury from fighting. The ESS in this game can be determined based on the values of \( V \) and \( C \).

## Mathematical Formalism
Let \( p \) be the proportion of the population using strategy \( S \) and \( 1-p \) be the proportion using strategy \( T \). The average payoff for strategy \( S \) in a population can be expressed as:

\[
E(S) = p \cdot P(S, S) + (1-p) \cdot P(S, T)
\]

Similarly, the average payoff for strategy \( T \) is:

\[
E(T) = p \cdot P(T, S) + (1-p) \cdot P(T, T)
\]

For \( S \) to be an ESS, it must satisfy the conditions outlined above, ensuring that it yields higher or equal payoffs compared to \( T \).

## Applications
The concept of ESS is widely applicable in various fields, including:
- **Biology**: Understanding animal behavior, mating strategies, and resource allocation.
- **Economics**: Analyzing competitive strategies in markets.
- **Sociology**: Studying social behaviors and norms.

## Conclusion
An Evolutionarily Stable Strategy (ESS) provides a framework for understanding how certain strategies can persist in a population over time, resisting invasions by alternative strategies. This concept is crucial for analyzing the dynamics of cooperation, competition, and adaptation in biological and social systems.

## References
- Maynard Smith, J. (1982). *Evolution and the Theory of Games*. Cambridge University Press.
- Hofbauer, J., & Sigmund, K. (1998). *Evolutionary Games and Population Dynamics*. Cambridge University Press.
- Nowak, M. A. (2006). *Evolutionary Dynamics: Exploring the Equations