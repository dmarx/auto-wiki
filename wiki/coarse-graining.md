
# Coarse Graining

## Definition
[[Coarse graining]] is a technique used in various fields such as statistical mechanics, information theory, and machine learning to simplify a complex system by reducing the number of degrees of freedom. This process involves grouping together similar states or variables into larger, more manageable units, thereby allowing for a more tractable analysis of the system's behavior.

## Mathematical Formalism
Let \( S \) be a system described by a set of variables \( \{x_1, x_2, \ldots, x_n\} \). Coarse graining can be represented mathematically by defining a mapping \( C: S \to S' \), where \( S' \) is the coarse-grained state space. The mapping \( C \) aggregates the original variables into a smaller set of variables \( \{y_1, y_2, \ldots, y_m\} \) such that:

\[
y_j = C(x_i) \quad \text{for } i \in I_j
\]

where \( I_j \) is a subset of indices corresponding to the original variables that are grouped together to form \( y_j \).

## Applications
1. **Statistical Mechanics**: In statistical mechanics, coarse graining is used to derive macroscopic properties from microscopic models. For example, one might average over the positions and momenta of particles in a gas to obtain thermodynamic quantities like pressure and temperature.

2. **Information Theory**: In information theory, coarse graining can be applied to reduce the complexity of probability distributions. By grouping events into larger categories, one can simplify the analysis of information content and entropy.

3. **Machine Learning**: In machine learning, coarse graining is often employed in feature extraction, where raw data is transformed into a lower-dimensional representation that captures the essential characteristics of the data while discarding noise.

## Symbolic Notation
Let \( P(x) \) be a probability distribution over the original state space \( S \). The coarse-grained probability distribution \( P'(y) \) can be expressed as:

\[
P'(y_j) = \sum_{i \in I_j} P(x_i)
\]

This equation shows how the probabilities of the original states are aggregated to form the probabilities of the coarse-grained states.

## Properties
- **Loss of Information**: Coarse graining typically results in a loss of information, as the details of the individual states are obscured in the process of aggregation.
- **Scale Dependence**: The choice of how to coarse grain can depend on the scale of observation. Different coarse-graining schemes may yield different effective theories or models.

## Further Reading
- [[Statistical Mechanics]]
- [[Entropy]]
- [[Feature Extraction]]
- [[Renormalization Group]]
- [[Phase Transitions]]
