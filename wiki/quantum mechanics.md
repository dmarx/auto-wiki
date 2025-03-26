
# Quantum Mechanics

## Overview
[[Quantum mechanics]] is a fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles. It provides a mathematical framework for understanding phenomena that cannot be explained by classical mechanics, such as the behavior of particles in a [[superposition]] of states and the concept of [[entanglement]].

## Mathematical Foundations

### State Vectors and Hilbert Spaces
In quantum mechanics, the state of a physical system is represented by a state vector \( |\psi\rangle \) in a complex vector space known as a [[Hilbert space]]. The inner product of two state vectors \( |\psi\rangle \) and \( |\phi\rangle \) is denoted as \( \langle \psi | \phi \rangle \), which provides a measure of the overlap between the two states.

### Operators and Observables
Physical observables, such as position \( \hat{x} \) and momentum \( \hat{p} \), are represented by linear operators acting on the state vectors in Hilbert space. The expectation value of an observable \( \hat{A} \) in a state \( |\psi\rangle \) is given by:

\[
\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
\]

### The Schrödinger Equation
The time evolution of a quantum state is governed by the [[Schrödinger equation]], which can be expressed in its time-dependent form as:

\[
i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle = \hat{H} |\psi(t)\rangle
\]

where \( \hbar \) is the reduced Planck's constant and \( \hat{H} \) is the Hamiltonian operator representing the total energy of the system.

## Quantum Superposition and Measurement

### Superposition Principle
The principle of superposition states that if \( |\psi_1\rangle \) and \( |\psi_2\rangle \) are valid quantum states, then any linear combination \( |\psi\rangle = c_1 |\psi_1\rangle + c_2 |\psi_2\rangle \) (where \( c_1, c_2 \in \mathbb{C} \)) is also a valid quantum state. This leads to phenomena such as [[quantum interference]].

### Measurement Postulate
Upon measurement of an observable \( \hat{A} \), the system collapses to one of the eigenstates \( |a_n\rangle \) of the operator \( \hat{A} \) with probability given by:

\[
P(a_n) = |\langle a_n | \psi \rangle|^2
\]

where \( P(a_n) \) is the probability of obtaining the measurement result \( a_n \).

## Quantum Entanglement
[[Entanglement]] is a phenomenon where two or more particles become correlated in such a way that the state of one particle cannot be described independently of the state of the other(s), even when the particles are separated by large distances. Mathematically, if two particles are in an entangled state, their joint state cannot be factored into individual states:

\[
|\psi\rangle_{AB} \neq |\psi\rangle_A \otimes |\psi\rangle_B
\]

## Quantum Field Theory
[[Quantum field theory]] (QFT) extends quantum mechanics to fields, treating particles as excitations of underlying fields. The mathematical formalism of QFT incorporates both quantum mechanics and special relativity, leading to the formulation of the [[Lagrangian]] and [[Hamiltonian]] densities, which describe the dynamics of fields.

## Conclusion
Quantum mechanics represents a paradigm shift in our understanding of the physical universe, challenging classical intuitions and providing a robust framework for the analysis of microscopic systems. Its implications extend beyond physics, influencing fields such as [[quantum computing]], [[quantum cryptography]], and the philosophy of science.

## References
- [[Dirac Notation]]
- [[Quantum Decoherence]]
- [[Bell's Theorem]]
- [[Many-Worlds Interpretation]]
