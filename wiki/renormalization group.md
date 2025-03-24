
# Renormalization Group

The [[renormalization group]] (RG) is a powerful mathematical framework used in theoretical physics and statistical mechanics to study systems with many degrees of freedom, particularly in the context of phase transitions and critical phenomena. It provides a systematic way to analyze how physical systems behave at different length scales and how the parameters of a theory change as one moves between these scales.

## Definition

The renormalization group involves a set of transformations that relate the behavior of a physical system at one scale to its behavior at another scale. The key idea is to "integrate out" the degrees of freedom associated with short-range fluctuations, leading to an effective theory that describes the long-range behavior of the system.

### Renormalization Procedure

1. **Coarse-Graining**: The first step in the RG process is to divide the system into blocks of size \( b \) (where \( b > 1 \)) and to average the properties of these blocks. This process effectively reduces the number of degrees of freedom in the system.

2. **Rescaling**: After coarse-graining, the system is rescaled to restore the original size. This involves redefining the parameters of the theory (e.g., coupling constants) to account for the changes introduced during coarse-graining.

3. **Fixed Points**: The RG flow can be visualized in terms of a flow diagram in the space of coupling constants. Fixed points in this space correspond to values of the parameters where the system exhibits scale invariance, meaning that the behavior of the system remains unchanged under further rescaling.

## Applications

The renormalization group has widespread applications in various fields, including:

1. **Statistical Mechanics**: RG is used to analyze phase transitions, such as the transition from a liquid to a gas. It helps to understand critical phenomena, where physical properties exhibit singular behavior.

2. **Quantum Field Theory**: In particle physics, RG techniques are employed to handle divergences in loop integrals and to relate the behavior of a quantum field theory at different energy scales.

3. **Condensed Matter Physics**: RG is crucial for studying critical phenomena in systems such as magnets, superconductors, and liquid crystals.

4. **Mathematics**: The RG framework has connections to various mathematical fields, including probability theory and dynamical systems.

## Mathematical Formulation

### RG Transformation

Consider a physical system described by a Hamiltonian \( H \) with coupling constants \( g \). The RG transformation can be expressed as:

\[
H' = H(g) \quad \text{with } g' = g'(g)
\]

where \( H' \) is the Hamiltonian after the RG transformation, and \( g' \) is the new set of coupling constants.

### Flow Equations

The behavior of the coupling constants under the RG transformation can be described by flow equations:

\[
\frac{dg}{d\ell} = \beta(g)
\]

where \( \ell \) is the logarithm of the length scale, and \( \beta(g) \) is the beta function that describes how the coupling constants change with scale. The fixed points of the flow equations are found by solving:

\[
\beta(g^*) = 0
\]

where \( g^* \) represents the fixed point values of the coupling constants.

## Example: Ising Model

The Ising model, which describes ferromagnetism in statistical mechanics, serves as a classic example of the application of the renormalization group. In the Ising model, the beta function can be derived, and the critical point can be analyzed using RG techniques to show how the system behaves near the phase transition.

## Conclusion

The renormalization group is a fundamental tool in understanding the behavior of complex systems across different scales. Its ability to connect microscopic interactions to macroscopic phenomena makes it indispensable in both theoretical physics and applied mathematics.

[[Phase Transitions]] | [[Critical Phenomena]] | [[Beta Function]]
