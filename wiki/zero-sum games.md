
# Zero-Sum Games

## Definition
A [[zero-sum game]] is a type of mathematical representation of a situation in which one participant's gain or loss is exactly balanced by the losses or gains of other participants. In other words, the total utility available in the game remains constant, hence the term "zero-sum." This concept is fundamental in game theory, a branch of mathematics that studies strategic interactions among rational decision-makers.

## Mathematical Formalism
In a zero-sum game involving two players, the payoffs can be represented in a matrix form. Let \( A \) be the payoff matrix for Player 1 (the maximizer) and \( B \) be the payoff matrix for Player 2 (the minimizer). The payoff for Player 1 can be expressed as:

\[
u = A(x, y)
\]

where:
- \( u \) is the utility or payoff for Player 1,
- \( x \) is the strategy chosen by Player 1,
- \( y \) is the strategy chosen by Player 2.

The condition for a zero-sum game is:

\[
u + v = 0
\]

where \( v \) is the payoff for Player 2, indicating that any gain by Player 1 results in an equivalent loss for Player 2.

### Example: Matching Pennies
Consider the game of matching pennies, where two players simultaneously choose heads or tails. The payoff matrix can be represented as follows:

\[
\begin{array}{c|c|c}
 & \text{Heads} & \text{Tails} \\
\hline
\text{Heads} & 1 & -1 \\
\hline
\text{Tails} & -1 & 1 \\
\end{array}
\]

In this matrix:
- If both players choose heads, Player 1 wins 1 (Player 2 loses 1).
- If Player 1 chooses heads and Player 2 chooses tails, Player 1 loses 1 (Player 2 wins 1), and so forth.

## Strategies
### Pure Strategies
A pure strategy is a strategy where a player makes a specific choice with certainty. In zero-sum games, players can adopt pure strategies, but these may not always lead to optimal outcomes.

### Mixed Strategies
A mixed strategy involves randomizing over possible moves, allowing players to make probabilistic choices. The optimal mixed strategy can be determined using the concept of expected utility. For a player \( i \) with mixed strategy \( p \), the expected utility can be expressed as:

\[
E(u) = \sum_{j} p_j A_{ij}
\]

where \( p_j \) is the probability of choosing strategy \( j \) and \( A_{ij} \) is the payoff associated with that strategy.

## Nash Equilibrium
In the context of zero-sum games, a [[Nash equilibrium]] occurs when both players have chosen strategies such that neither player can benefit by unilaterally changing their strategy. In zero-sum games, the Nash equilibrium can often be found using linear programming techniques or by solving the corresponding dual problem.

## Applications
Zero-sum games have applications in various fields, including:
- **Economics**: Modeling competitive markets where one party's gain is another's loss.
- **Political Science**: Analyzing conflicts and negotiations between competing entities.
- **Computer Science**: Developing algorithms for strategic decision-making in artificial intelligence.

## Conclusion
Zero-sum games provide a foundational framework for understanding competitive interactions where resources are limited and outcomes are directly opposed. The mathematical rigor of game theory allows for the analysis of strategies and outcomes, making it a vital tool in economics, political science, and beyond.

## References
- von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
- Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press.

[[Game Theory]] | [[Nash Equilibrium]] | [[Mixed Strategies]]
