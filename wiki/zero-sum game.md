
# Zero-Sum Game

A [[zero-sum game]] is a fundamental concept in game theory, a branch of mathematics that studies strategic interactions among rational decision-makers. In a zero-sum game, the total utility or payoff available to all players remains constant, meaning that any gain by one player results in an equivalent loss by another player. This characteristic makes zero-sum games particularly relevant in competitive scenarios.

## Definition

Formally, a zero-sum game can be defined as follows:

- Let \( n \) players be involved in the game, and let \( u_i \) denote the utility (or payoff) received by player \( i \).
- The game is zero-sum if the sum of the payoffs for all players is zero:

\[
\sum_{i=1}^{n} u_i = 0
\]

This implies that if one player increases their payoff by a certain amount, the total payoff for the other players decreases by the same amount.

## Representation

Zero-sum games can be represented using a payoff matrix, particularly in two-player scenarios. Consider a game with two players, Player A and Player B. The strategies available to Player A can be represented in rows, while the strategies available to Player B can be represented in columns. The entries of the matrix represent the payoffs for Player A, while the corresponding losses for Player B are the negative of these values.

### Example Payoff Matrix

\[
\begin{array}{c|c|c}
 & B_1 & B_2 \\
\hline
A_1 & a_{11} & a_{12} \\
\hline
A_2 & a_{21} & a_{22} \\
\end{array}
\]

In this matrix:
- \( a_{ij} \) represents the payoff to Player A when Player A chooses strategy \( A_i \) and Player B chooses strategy \( B_j \).
- The payoff to Player B is \( -a_{ij} \).

## Strategies

In zero-sum games, players can adopt different strategies:

1. **Pure Strategies**: A player chooses a specific strategy with certainty. For example, Player A may always choose \( A_1 \).

2. **Mixed Strategies**: A player randomizes over their available strategies, assigning probabilities to each strategy. For instance, Player A may choose \( A_1 \) with probability \( p \) and \( A_2 \) with probability \( 1-p \).

The expected payoff for Player A when using a mixed strategy can be calculated as:

\[
E(u) = p \cdot (a_{11} \cdot q_1 + a_{12} \cdot q_2) + (1-p) \cdot (a_{21} \cdot q_1 + a_{22} \cdot q_2)
\]

where \( q_j \) is the probability that Player B chooses strategy \( B_j \).

## Nash Equilibrium

In the context of zero-sum games, a [[Nash equilibrium]] occurs when both players have chosen their strategies such that neither player can unilaterally improve their payoff by changing their strategy. In zero-sum games, the Nash equilibrium can often be found using linear programming techniques or by solving the corresponding minimax problem:

\[
\max_{p} \min_{q} E(u)
\]

This formulation seeks to maximize the minimum expected payoff for Player A, ensuring that Player B's strategy minimizes Player A's payoff.

## Applications

Zero-sum games have applications in various fields, including:

- **Economics**: Analyzing competitive markets where one firm's gain is another firm's loss.
- **Political Science**: Studying conflicts and negotiations between competing parties.
- **Computer Science**: Developing algorithms for strategic decision-making in artificial intelligence and machine learning.

## Conclusion

Zero-sum games provide a foundational framework for understanding competitive interactions where resources are limited and outcomes are directly opposed. The mathematical tools developed for analyzing these games have far-reaching implications across multiple disciplines.

[[Game Theory]] | [[Nash Equilibrium]] | [[Mixed Strategy]]
