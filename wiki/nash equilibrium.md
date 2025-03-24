
# Nash Equilibrium

## Definition
A Nash Equilibrium is a concept in game theory that represents a situation in which no player can benefit by unilaterally changing their strategy, given that the other players' strategies remain unchanged. In other words, each player's strategy is optimal given the strategies of all other players. The concept is named after mathematician [[John Nash]], who introduced it in his 1950 dissertation.

## Key Concepts

### 1. **Game Structure**
A game consists of:
- **Players**: The decision-makers in the game.
- **Strategies**: The possible actions each player can take.
- **Payoffs**: The outcomes associated with each combination of strategies, typically represented in a payoff matrix.

### 2. **Mathematical Representation**
Consider a game with \( n \) players, where each player \( i \) has a set of strategies \( S_i \). The payoff for player \( i \) when players choose strategies \( s = (s_1, s_2, \ldots, s_n) \) is denoted as \( u_i(s) \).

A strategy profile \( s^* = (s_1^*, s_2^*, \ldots, s_n^*) \) is a Nash Equilibrium if:

\[
u_i(s^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i
\]

where \( s_{-i}^* \) represents the strategies of all players other than player \( i \).

### 3. **Pure vs. Mixed Strategies**
- **Pure Strategy**: A strategy where a player chooses a specific action with certainty.
- **Mixed Strategy**: A strategy where a player randomizes over possible actions, assigning a probability to each action.

A Nash Equilibrium can exist in pure strategies, mixed strategies, or both. The mixed strategy Nash Equilibrium is particularly useful in games where no pure strategy equilibrium exists.

### 4. **Existence of Nash Equilibrium**
The existence of at least one Nash Equilibrium is guaranteed in finite games by [[Nash's Existence Theorem]], which states that every finite game has at least one Nash Equilibrium in mixed strategies.

## Example: The Prisoner's Dilemma
The Prisoner's Dilemma is a classic example illustrating the concept of Nash Equilibrium. In this game, two players can either cooperate (C) or defect (D). The payoff matrix is as follows:

\[
\begin{array}{c|c|c}
 & C & D \\
\hline
C & (R, R) & (S, T) \\
\hline
D & (T, S) & (P, P) \\
\end{array}
\]

where:
- \( R \): Reward for mutual cooperation
- \( T \): Temptation to defect
- \( S \): Sucker's payoff for cooperating while the other defects
- \( P \): Punishment for mutual defection

In the Prisoner's Dilemma, the Nash Equilibrium occurs when both players choose to defect (D, D), as neither player can improve their payoff by unilaterally changing their strategy.

## Applications
Nash Equilibrium has applications across various fields, including:
- **Economics**: Analyzing competitive markets and oligopolies.
- **Political Science**: Studying voting strategies and coalition formation.
- **Biology**: Understanding evolutionary stable strategies in populations.

## Conclusion
The Nash Equilibrium is a foundational concept in game theory that provides insights into strategic interactions among rational players. By understanding the conditions under which players reach equilibrium, researchers can analyze a wide range of competitive and cooperative scenarios.

## References
- Nash, J. F. (1950). "Equilibrium Points in N-Person Games." *Proceedings of the National Academy of Sciences*.
- Myerson, R. B. (1991). *Game Theory: Analysis of Conflict*. Harvard University Press.
- Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press.

[[Game Theory]] | [[Nash's Existence Theorem]] | [[Prisoner's Dilemma]]
