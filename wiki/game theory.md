
# Game Theory

## Definition
Game theory is a mathematical framework for analyzing situations in which multiple agents (players) make decisions that affect each other's outcomes. It provides tools for understanding strategic interactions, where the choices of one player depend on the choices of others. Game theory is widely applied in economics, political science, biology, and computer science.

## Key Concepts
1. **Players**: The decision-makers in a game, each with their own strategies and payoffs.

2. **Strategies**: A strategy is a complete plan of action that specifies the choices a player will make in every possible situation within the game. Strategies can be:
   - **Pure Strategy**: A specific choice made by a player.
   - **Mixed Strategy**: A probability distribution over possible pure strategies.

3. **Payoffs**: The outcomes associated with each combination of strategies chosen by the players, typically represented in a payoff matrix or as utility functions.

4. **Games**: Games can be classified based on various criteria:
   - **Cooperative vs. Non-Cooperative**: Cooperative games allow for binding agreements, while non-cooperative games do not.
   - **Zero-Sum vs. Non-Zero-Sum**: In zero-sum games, one player's gain is another player's loss. Non-zero-sum games allow for mutual gains or losses.
   - **Simultaneous vs. Sequential**: In simultaneous games, players make decisions at the same time, while in sequential games, players make decisions one after another.

## Mathematical Formalism
Game theory can be formalized using various mathematical notations and structures:

### Normal Form Representation
A game can be represented in normal form using a payoff matrix. For a two-player game with players \( A \) and \( B \), the payoff matrix can be expressed as:
\[
\begin{array}{c|c|c}
 & B_1 & B_2 \\
\hline
A_1 & (u_{A1}, v_{B1}) & (u_{A2}, v_{B2}) \\
\hline
A_2 & (u_{A3}, v_{B3}) & (u_{A4}, v_{B4}) \\
\end{array}
\]
where \( u_{Ai} \) represents the payoff to player \( A \) and \( v_{Bi} \) represents the payoff to player \( B \) for each combination of strategies.

### Extensive Form Representation
Games can also be represented in extensive form using game trees, which illustrate the sequential nature of decisions. Each node represents a decision point, and branches represent possible actions.

### Nash Equilibrium
A key concept in game theory is the Nash equilibrium, a situation where no player can benefit from unilaterally changing their strategy, given the strategies of the other players. Formally, a strategy profile \( (s_1^*, s_2^*, \ldots, s_n^*) \) is a Nash equilibrium if:
\[
u_i(s_1^*, s_2^*, \ldots, s_n^*) \geq u_i(s_1, s_2, \ldots, s_n^*) \quad \forall s_i \in S_i
\]
where \( u_i \) is the utility function for player \( i \) and \( S_i \) is the strategy set for player \( i \).

## Applications
Game theory has a wide range of applications, including:
- **Economics**: Analyzing market competition, auctions, and bargaining situations.
- **Political Science**: Studying voting systems, coalition formation, and international relations.
- **Biology**: Understanding evolutionary strategies and animal behavior through concepts like the [[Evolutionarily Stable Strategy (ESS)]].
- **Computer Science**: Designing algorithms for network routing, resource allocation, and multi-agent systems.

## Conclusion
Game theory provides a powerful framework for analyzing strategic interactions among rational agents. Its mathematical rigor and broad applicability make it an essential tool in various fields, helping to understand and predict behavior in competitive and cooperative environments.

## Related Concepts
- [[Nash Equilibrium]]
- [[Cooperative Game Theory]]
- [[Zero-Sum Games]]
- [[Evolutionarily Stable Strategy (ESS)]]
- [[Payoff Matrix]]
