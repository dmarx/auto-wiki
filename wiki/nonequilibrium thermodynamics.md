
# Nonequilibrium Thermodynamics

## Definition
Nonequilibrium thermodynamics is the branch of thermodynamics that deals with systems that are not in thermodynamic equilibrium. Unlike equilibrium thermodynamics, which focuses on systems where macroscopic properties are stable and uniform, nonequilibrium thermodynamics studies the dynamics of systems undergoing changes, where gradients in temperature, pressure, and chemical potential drive processes.

## Fundamental Concepts
1. **Thermodynamic Equilibrium**: A state where macroscopic properties (temperature, pressure, volume) are uniform throughout the system and do not change over time. In equilibrium, the system is characterized by a maximum entropy state.

2. **Nonequilibrium States**: Systems that exhibit spatial or temporal gradients in their properties. These gradients lead to the flow of energy and matter, resulting in irreversible processes.

3. **Irreversibility**: In nonequilibrium thermodynamics, processes are typically irreversible, meaning they cannot spontaneously return to their original state without external intervention. This is often quantified using the concept of entropy production.

## Mathematical Framework
The mathematical treatment of nonequilibrium thermodynamics often involves the following key equations and principles:

### 1. **Entropy Production**
The rate of entropy production (\( \sigma \)) in a nonequilibrium system can be expressed as:
\[
\sigma = \sum_i \frac{J_i}{X_i}
\]
where:
- \( J_i \) is the flux of the \( i \)-th process (e.g., heat flow, mass transfer),
- \( X_i \) is the thermodynamic force associated with that process (e.g., temperature gradient, concentration gradient).

### 2. **Linear Response Theory**
In many cases, the relationship between fluxes and forces can be linearized around equilibrium. This leads to the phenomenological equations:
\[
J_i = L_{ij} X_j
\]
where:
- \( L_{ij} \) are the phenomenological coefficients that relate the fluxes to the thermodynamic forces.

### 3. **Continuity Equation**
The continuity equation describes the conservation of mass in a system and can be expressed as:
\[
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0
\]
where:
- \( \rho \) is the density of the substance,
- \( \mathbf{J} \) is the flux vector.

### 4. **Energy Balance**
The energy balance in a nonequilibrium system can be described by the first law of thermodynamics, which states:
\[
\frac{dU}{dt} = Q - W + \sum_i \mu_i J_i
\]
where:
- \( U \) is the internal energy,
- \( Q \) is the heat added to the system,
- \( W \) is the work done by the system,
- \( \mu_i \) is the chemical potential.

## Applications
Nonequilibrium thermodynamics has a wide range of applications, including:
- **Biological Systems**: Understanding metabolic processes and energy transfer in living organisms.
- **Material Science**: Studying phase transitions and the behavior of materials under stress.
- **Chemical Engineering**: Designing reactors and separation processes that operate far from equilibrium.

## Related Concepts
- [[Entropy Production]]
- [[Irreversibility]]
- [[Linear Response Theory]]
- [[Phase Transitions]]
- [[Transport Phenomena]]

## Conclusion
Nonequilibrium thermodynamics provides a comprehensive framework for understanding the behavior of systems that are not in equilibrium. By analyzing the interactions between thermodynamic forces and fluxes, it allows for the prediction and modeling of complex processes across various scientific and engineering disciplines.
