
# Maxwell Relations

## Definition
[[Maxwell relations]] are a set of equations in thermodynamics that describe the relationships between different thermodynamic potentials and their derivatives. These relations arise from the equality of mixed partial derivatives of state functions, reflecting the interdependence of thermodynamic variables. They are particularly useful for deriving relationships between measurable quantities without direct measurement.

## Derivation
Maxwell relations can be derived from the fundamental thermodynamic equations. The most common thermodynamic potentials are the [[Gibbs free energy]] (\( G \)) and the [[Helmholtz free energy]] (\( F \)). The differential forms of these potentials can be expressed as:

1. **Gibbs Free Energy**:
   \[
   dG = -S dT + V dP
   \]

2. **Helmholtz Free Energy**:
   \[
   dF = -S dT - P dV
   \]

3. **Internal Energy**:
   \[
   dU = T dS - P dV
   \]

4. **Enthalpy**:
   \[
   dH = T dS + V dP
   \]

### Mixed Partial Derivatives
From these differential forms, we can apply the equality of mixed partial derivatives. For example, starting with the Gibbs free energy:

\[
\left( \frac{\partial G}{\partial P} \right)_T = V \quad \text{and} \quad \left( \frac{\partial G}{\partial T} \right)_P = -S
\]

By applying the equality of mixed partial derivatives, we obtain the first Maxwell relation:

\[
\left( \frac{\partial S}{\partial P} \right)_T = \left( \frac{\partial V}{\partial T} \right)_P
\]

This process can be repeated for the other potentials to derive additional Maxwell relations.

## List of Maxwell Relations
The following are the commonly used Maxwell relations derived from the four thermodynamic potentials:

1. From Gibbs Free Energy:
   \[
   \left( \frac{\partial S}{\partial P} \right)_T = \left( \frac{\partial V}{\partial T} \right)_P
   \]

2. From Helmholtz Free Energy:
   \[
   \left( \frac{\partial P}{\partial T} \right)_V = -\left( \frac{\partial S}{\partial V} \right)_T
   \]

3. From Internal Energy:
   \[
   \left( \frac{\partial S}{\partial V} \right)_T = \left( \frac{\partial P}{\partial T} \right)_V
   \]

4. From Enthalpy:
   \[
   \left( \frac{\partial V}{\partial T} \right)_P = \left( \frac{\partial S}{\partial P} \right)_T
   \]

## Applications
Maxwell relations are instrumental in various applications within thermodynamics:

- **Calculating Thermodynamic Properties**: They allow for the calculation of one thermodynamic property in terms of others, facilitating experimental measurements.
- **Phase Transitions**: Maxwell relations can be used to analyze systems undergoing phase changes, providing insights into latent heat and other properties.
- **Statistical Mechanics**: They bridge macroscopic thermodynamic properties with microscopic behavior, enhancing the understanding of systems at the molecular level.

## Conclusion
Maxwell relations are a powerful tool in thermodynamics, providing essential connections between different thermodynamic variables. Their derivation from fundamental thermodynamic potentials highlights the interrelated nature of thermodynamic properties, making them invaluable for both theoretical analysis and practical applications.

## References
- Callen, H. B. (1985). *Thermodynamics and an Introduction to Thermostatistics*. Wiley.
- Atkins, P. W., & de Paula, J. (2010). *Physical Chemistry*. Oxford University Press.

[[Thermodynamics]] | [[Gibbs Free Energy]] | [[Helmholtz Free Energy]]
