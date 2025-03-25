
# Evolutionary Game Theory

## Definition
**Evolutionary Game Theory (EGT)** is a theoretical framework that combines concepts from evolutionary biology and game theory to study the strategic interactions among individuals in populations. It focuses on how the strategies of individuals evolve over time through the process of natural selection, emphasizing the role of competition, cooperation, and the dynamics of strategy adoption.

## Mathematical Formulation
In EGT, the population is typically represented by a set of strategies, each associated with a payoff that reflects the success of that strategy in a given environment. The basic components of EGT include:

1. **Strategy Set**: Let \( S = \{s_1, s_2, \ldots, s_n\} \) be the set of strategies available to individuals in the population.

2. **Payoff Matrix**: The interactions between strategies can be represented by a payoff matrix \( A \), where the entry \( A_{ij} \) denotes the payoff received by an individual using strategy \( s_i \) when interacting with an individual using strategy \( s_j \).

3. **Population Dynamics**: The frequency of each strategy in the population can be represented by a vector \( \mathbf{x} = (x_1, x_2, \ldots, x_n) \), where \( x_i \) is the proportion of individuals using strategy \( s_i \) such that \( \sum_{i=1}^{n} x_i = 1 \).

### Replicator Dynamics
The evolution of strategy frequencies over time can be modeled using **replicator dynamics**, which describe how the proportion of individuals using a particular strategy changes based on their relative payoffs. The replicator equation for strategy \( s_i \) is given by:

\[
\dot{x}_i = x_i \left( f_i(\mathbf{x}) - \bar{f}(\mathbf{x}) \right)
\]

where:
- \( \dot{x}_i \) is the time derivative of the frequency of strategy \( s_i \),
- \( f_i(\mathbf{x}) = \sum_{j} A_{ij} x_j \) is the expected payoff of strategy \( s_i \),
- \( \bar{f}(\mathbf{x}) = \sum_{k} f_k(\mathbf{x}) x_k \) is the average payoff in the population.

## Nash Equilibrium and Evolutionarily Stable Strategies
### Nash Equilibrium
A strategy profile is a **Nash equilibrium** if no individual can benefit by unilaterally changing their strategy, given the strategies of others. In EGT, Nash equilibria can be interpreted as stable states of the population where strategies do not change over time.

### Evolutionarily Stable Strategy (ESS)
An **evolutionarily stable strategy** is a refinement of Nash equilibrium that accounts for the dynamics of strategy adoption. A strategy \( s^* \) is an ESS if:
1. It is a Nash equilibrium.
2. If a small proportion of mutants using a different strategy \( s_m \) invade the population, the payoff of \( s^* \) against \( s_m \) must be greater than or equal to the payoff of \( s_m \) against itself.

Mathematically, this can be expressed as:

\[
f_{s^*}(s^*) > f_{s^*}(s_m) \quad \text{or} \quad f_{s^*}(s^*) = f_{s^*}(s_m) \text{ and } f_{s^*}(s^*) > f_{s_m}(s_m)
\]

## Applications
Evolutionary game theory has applications across various fields, including:
- **Biology**: Understanding the evolution of cooperation, altruism, and competition among species.
- **Economics**: Analyzing market behaviors, pricing strategies, and the evolution of firms in competitive environments.
- **Social Sciences**: Studying the dynamics of social norms, cultural evolution, and the emergence of cooperation in human societies.

## Conclusion
Evolutionary game theory provides a robust framework for analyzing the strategic interactions of individuals in populations, emphasizing the evolutionary dynamics of strategy adoption. Its interdisciplinary applications make it a valuable tool for understanding complex adaptive systems.

## Related Concepts
- [[Game Theory]]
- [[Nash Equilibrium]]
- [[Evolutionarily Stable Strategy (ESS)]]
- [[Replicator Dynamics]]
- [[Cooperative Game Theory]]
- [[Population Dynamics]]
