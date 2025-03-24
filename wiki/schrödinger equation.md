
# Schrödinger Equation

## Definition
The [[Schrödinger Equation]] is a fundamental equation in quantum mechanics that describes how the quantum state of a physical system changes over time. It is a key result of quantum theory and provides a mathematical framework for understanding the behavior of particles at the quantum level. The equation is named after the physicist Erwin Schrödinger, who formulated it in 1925.

## Formulation

### Time-Dependent Schrödinger Equation
The time-dependent Schrödinger equation describes the evolution of a quantum state \( \psi(x, t) \) as a function of position \( x \) and time \( t \). It is given by:

\[
i\hbar \frac{\partial \psi(x, t)}{\partial t} = \hat{H} \psi(x, t)
\]

where:
- \( i \) is the imaginary unit,
- \( \hbar \) (h-bar) is the reduced Planck's constant, defined as \( \hbar = \frac{h}{2\pi} \),
- \( \hat{H} \) is the Hamiltonian operator, which represents the total energy of the system.

### Time-Independent Schrödinger Equation
In many cases, particularly for systems with time-independent potentials, the time-independent Schrödinger equation can be used. It is derived from the time-dependent equation by separating variables and is expressed as:

\[
\hat{H} \psi(x) = E \psi(x)
\]

where:
- \( E \) is the energy eigenvalue associated with the state \( \psi(x) \).

The Hamiltonian operator \( \hat{H} \) typically takes the form:

\[
\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x)
\]

where:
- \( m \) is the mass of the particle,
- \( V(x) \) is the potential energy as a function of position.

## Interpretation
The wave function \( \psi(x, t) \) contains all the information about the quantum state of the system. The square of the absolute value of the wave function, \( |\psi(x, t)|^2 \), gives the probability density of finding a particle at position \( x \) at time \( t \):

\[
P(x, t) = |\psi(x, t)|^2
\]

## Applications
The Schrödinger equation is used to model a wide range of physical systems, including:
- **Quantum Mechanics**: Describing the behavior of electrons in atoms and molecules.
- **Quantum Chemistry**: Analyzing chemical reactions and molecular structures.
- **Solid State Physics**: Understanding the properties of solids, including band theory and superconductivity.

## Related Concepts
- [[Quantum Mechanics]]
- [[Wave Function]]
- [[Hamiltonian Operator]]
- [[Quantum States]]

## Further Reading
- [[Introduction to Quantum Mechanics]]
- [[Applications of the Schrödinger Equation]]
- [[Time Evolution in Quantum Mechanics]]
