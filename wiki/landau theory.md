
# Landau Theory

## Overview
Landau theory, named after the physicist [[Lev Landau]], is a theoretical framework used to describe phase transitions and critical phenomena in statistical mechanics and condensed matter physics. It provides a systematic approach to understanding how physical systems change from one phase to another, particularly near critical points where the properties of the system exhibit significant changes.

## Free Energy and Order Parameters
At the heart of Landau theory is the concept of the [[free energy]] \( F \), which is a thermodynamic potential that measures the work obtainable from a thermodynamic system at constant temperature and volume. The free energy can be expressed as a function of an [[order parameter]] \( \phi \), which characterizes the state of the system. The order parameter is typically zero in one phase and non-zero in another, indicating a symmetry breaking.

The free energy can be expanded in a Taylor series around the equilibrium value of the order parameter:

\[
F(\phi) = F_0 + a(T) \phi^2 + b \phi^4 + \ldots
\]

where:
- \( F_0 \) is the free energy at the reference state,
- \( a(T) \) is a coefficient that depends on temperature \( T \),
- \( b \) is a positive constant ensuring stability of the free energy.

### Coefficient \( a(T) \)
The coefficient \( a(T) \) typically has the form:

\[
a(T) = a_0 (T - T_c)
\]

where \( T_c \) is the critical temperature at which the phase transition occurs. For \( T < T_c \), \( a(T) < 0 \), leading to a non-zero equilibrium value of the order parameter \( \phi \).

## Phase Transitions
Landau theory classifies phase transitions into two main types:

1. **First-Order Transitions**: These transitions involve a discontinuity in the first derivative of the free energy (e.g., volume, entropy) with respect to some thermodynamic variable. In this case, the free energy has multiple minima, and the system can exist in different phases.

2. **Second-Order Transitions**: These transitions are characterized by continuous changes in the first derivatives of the free energy, but a discontinuity in the second derivatives (e.g., heat capacity). Near the critical point, the order parameter changes continuously.

## Symmetry and Group Theory
Landau theory heavily relies on the concepts of symmetry and group theory. The order parameter is associated with the symmetry of the system. As the system undergoes a phase transition, the symmetry may be broken, leading to a new phase with different properties.

### Landau-Ginzburg Free Energy
In more complex systems, the Landau theory can be extended to include spatial variations of the order parameter, leading to the [[Landau-Ginzburg]] theory. The free energy density can be expressed as:

\[
\mathcal{F} = \frac{1}{2} (\nabla \phi)^2 + F(\phi)
\]

where \( \nabla \phi \) represents the spatial gradient of the order parameter, allowing for the study of spatially inhomogeneous phases and fluctuations.

## Applications
Landau theory has been successfully applied to various physical systems, including:
- [[Superconductivity]]: Describing the transition from normal to superconducting states.
- [[Magnetism]]: Understanding ferromagnetic and antiferromagnetic transitions.
- [[Liquid Crystals]]: Analyzing the phase behavior of liquid crystal materials.

## Conclusion
Landau theory provides a powerful framework for understanding phase transitions through the lens of free energy and order parameters. Its reliance on symmetry principles and mathematical formalism allows for a deep exploration of critical phenomena in various physical systems.

## References
- Landau, L. D., & Lifshitz, E. M. (1980). *Statistical Physics*.
- Goldenfeld, N. (1992). *Lectures on Phase Transitions and the Renormalization Group*.
