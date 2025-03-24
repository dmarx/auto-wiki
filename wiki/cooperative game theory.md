
# Cooperative Game Theory

## Definition
Cooperative game theory is a branch of game theory that studies how groups of players can coordinate their strategies to achieve better outcomes than they could individually. In cooperative games, players can form binding agreements and coalitions, allowing them to share the benefits of cooperation.

## Key Concepts

### 1. **Coalitions**
A coalition is a subset of players who agree to work together to achieve a common goal. The set of all possible coalitions in a game with \( n \) players is denoted as \( 2^N \), where \( N \) is the set of players.

### 2. **Characteristic Function**
The characteristic function \( v: 2^N \rightarrow \mathbb{R} \) assigns a value to each coalition, representing the total worth or payoff that the coalition can achieve by cooperating. For a coalition \( S \subseteq N \), \( v(S) \) indicates the maximum payoff that coalition \( S \) can secure.

### 3. **Core**
The core is a solution concept in cooperative game theory that represents the set of feasible allocations of payoffs to players such that no coalition has an incentive to deviate. An allocation \( (x_1, x_2, \ldots, x_n) \) is in the core if:

\[
\sum_{i \in S} x_i \geq v(S) \quad \forall S \subseteq N
\]

where \( x_i \) is the payoff to player \( i \).

### 4. **Shapley Value**
The Shapley value is a method for distributing the total gains from cooperation among players based on their marginal contributions. The Shapley value \( \phi_i \) for player \( i \) is defined as:

\[
\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (|N| - |S| - 1)!}{|N|!} \left( v(S \cup \{i\}) - v(S) \right)
\]

where \( |S| \) is the number of players in coalition \( S \) and \( |N| \) is the total number of players.

### 5. **Nash Bargaining Solution**
The Nash bargaining solution is a solution concept for cooperative games that focuses on the negotiation process between players. It is defined by the following axioms:
- **Pareto Efficiency**: The solution must be Pareto optimal.
- **Symmetry**: If players are symmetric, they should receive symmetric payoffs.
- **Invariance**: The solution should remain unchanged under affine transformations of the utility functions.
- **Independence of Irrelevant Alternatives**: The solution should depend only on the relevant alternatives.

## Applications
Cooperative game theory has applications in various fields, including:
- **Economics**: Analyzing market structures and cooperative behavior among firms.
- **Political Science**: Studying coalition formation in legislatures and political parties.
- **Network Theory**: Understanding cooperation in networks, such as communication or transportation networks.
- **Resource Allocation**: Distributing resources among agents in a fair and efficient manner.

## Mathematical Formalism
Cooperative games can be represented mathematically using the following notation:
- Let \( N = \{1, 2, \ldots, n\} \) be the set of players.
- Let \( v: 2^N \rightarrow \mathbb{R} \) be the characteristic function.
- An allocation \( x \in \mathbb{R}^n \) is a vector where \( x_i \) is the payoff to player \( i \).

The core can be expressed as:

\[
\text{Core} = \{ x \in \mathbb{R}^n : \sum_{i \in S} x_i \geq v(S) \quad \forall S \subseteq N, \sum_{i=1}^n x_i = v(N) \}
\]

## Conclusion
Cooperative game theory provides a framework for understanding how players can work together to achieve better outcomes through cooperation. By analyzing coalitions, payoffs, and solution concepts like the core and Shapley value, researchers can gain insights into strategic interactions in various domains.

## References
- Shapley, L. S. (1953). "A Value for n-Person Games." In *Contributions to the Theory of Games*, Volume II, 307-317. Princeton University Press.
- von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
- Maschler, M., Peleg, B., & Shapley, L. S. (1979). *The Game Theoretic Approach to Cooperative Games*. In *Game Theory