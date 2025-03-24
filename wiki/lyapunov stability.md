
# Lyapunov Stability

## Overview
Lyapunov stability is a concept in the field of dynamical systems that assesses the stability of equilibrium points. It is named after the Russian mathematician [[Alexandr Lyapunov]], who developed the theory in the late 19th century. The primary goal of Lyapunov stability analysis is to determine whether a system will return to equilibrium after a small perturbation.

## Definitions
1. **Equilibrium Point**: A point \( x^* \) in the state space of a dynamical system where the system remains at rest if it starts there. Mathematically, for a system described by \( \dot{x} = f(x) \), \( x^* \) is an equilibrium point if \( f(x^*) = 0 \).

2. **Lyapunov Stability**: An equilibrium point \( x^* \) is said to be **stable** if, for every \( \epsilon > 0 \), there exists a \( \delta > 0 \) such that if the initial state \( x(0) \) satisfies \( \| x(0) - x^* \| < \delta \), then the state remains within \( \epsilon \) of \( x^* \) for all future times \( t \geq 0 \):
   \[
   \| x(t) - x^* \| < \epsilon \quad \forall t \geq 0
   \]

3. **Asymptotic Stability**: An equilibrium point \( x^* \) is **asymptotically stable** if it is stable and, in addition, there exists a \( \delta > 0 \) such that if \( \| x(0) - x^* \| < \delta \), then \( x(t) \to x^* \) as \( t \to \infty \).

4. **Instability**: An equilibrium point is considered **unstable** if it is not stable.

## Lyapunov's Direct Method
Lyapunov's direct method provides a systematic way to assess stability without solving the differential equations governing the system. The method involves the construction of a **Lyapunov function** \( V: \mathbb{R}^n \to \mathbb{R} \), which is a scalar function that satisfies certain properties.

### Properties of Lyapunov Functions
1. **Positive Definiteness**: \( V(x) > 0 \) for all \( x \neq x^* \) and \( V(x^*) = 0 \).
2. **Radially Unbounded**: \( V(x) \to \infty \) as \( \| x \| \to \infty \).
3. **Derivative Condition**: The time derivative of \( V \) along the trajectories of the system, denoted as \( \dot{V}(x) = \frac{dV}{dt} \), must satisfy:
   - For stability: \( \dot{V}(x) \leq 0 \)
   - For asymptotic stability: \( \dot{V}(x) < 0 \)

### Example
Consider the linear system described by:
\[
\dot{x} = Ax
\]
where \( A \) is a matrix. A common choice for the Lyapunov function is:
\[
V(x) = x^T P x
\]
where \( P \) is a symmetric positive definite matrix. The derivative is given by:
\[
\dot{V}(x) = x^T (A^T P + PA) x
\]
If \( A \) is stable (i.e., all eigenvalues have negative real parts), then there exists a matrix \( P \) such that \( A^T P + PA \) is negative definite, ensuring asymptotic stability.

## Applications
Lyapunov stability has applications across various fields, including:
- Control theory, where it is used to design stable control systems.
- Robotics, for ensuring stability in motion planning.
- Economics, in the analysis of equilibrium points in economic models.

## Related Concepts
- [[Dynamical Systems]]
- [[Control Theory]]
- [[Stability Theory]]
- [[Nonlinear Systems]]

## Conclusion
Lyapunov stability provides a powerful framework for analyzing the stability of dynamical systems without requiring explicit solutions to the governing equations. The construction of appropriate Lyapunov functions is central to this analysis, enabling researchers and practitioners to ensure system robustness in various applications.

