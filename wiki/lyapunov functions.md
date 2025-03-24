
# Lyapunov Functions

## Definition
A [[Lyapunov function]] is a scalar function \( V: \mathbb{R}^n \to \mathbb{R} \) that is used to prove the stability of an equilibrium point in a dynamical system. Specifically, for a dynamical system described by the ordinary differential equation (ODE):

\[
\dot{x} = f(x)
\]

where \( x \in \mathbb{R}^n \) and \( f: \mathbb{R}^n \to \mathbb{R}^n \), a Lyapunov function \( V(x) \) is typically required to satisfy the following conditions:

1. **Positive Definiteness**: \( V(x) > 0 \) for all \( x \neq 0 \) and \( V(0) = 0 \).
2. **Continuity**: \( V(x) \) is continuous in \( \mathbb{R}^n \).
3. **Differentiability**: \( V(x) \) is differentiable in a neighborhood of the equilibrium point.
4. **Decreasing Condition**: The time derivative of \( V \) along the trajectories of the system, denoted as \( \dot{V}(x) \), must satisfy \( \dot{V}(x) = \nabla V(x) \cdot f(x) < 0 \) for all \( x \) in a neighborhood of the equilibrium point (except at the equilibrium itself).

## Purpose
Lyapunov functions are primarily used in the context of stability analysis. They provide a method to demonstrate that the equilibrium point \( x = 0 \) is stable, asymptotically stable, or unstable without solving the differential equations explicitly.

### Stability Types
- **Stable**: If \( V(x) \) is positive definite and \( \dot{V}(x) \leq 0 \), the equilibrium is stable.
- **Asymptotically Stable**: If \( V(x) \) is positive definite and \( \dot{V}(x) < 0 \), the equilibrium is asymptotically stable.
- **Unstable**: If \( V(x) \) does not satisfy the above conditions, the equilibrium may be unstable.

## Examples
1. **Quadratic Lyapunov Function**: A common choice for a Lyapunov function is a quadratic form:

\[
V(x) = x^T P x
\]

where \( P \) is a positive definite matrix. The derivative along the system's trajectory is given by:

\[
\dot{V}(x) = \nabla V(x) \cdot f(x) = x^T (P f(x) + f(x)^T P) 
\]

2. **Pendulum Example**: For a simple pendulum described by the equation:

\[
\dot{\theta} = \omega, \quad \dot{\omega} = -\frac{g}{L} \sin(\theta)
\]

a suitable Lyapunov function can be:

\[
V(\theta, \omega) = \frac{1}{2} m g L (1 - \cos(\theta)) + \frac{1}{2} m L^2 \omega^2
\]

This function represents the total mechanical energy of the system, which is positive definite and can be shown to decrease over time, indicating stability.

## Applications
Lyapunov functions are widely used in various fields, including:
- Control theory for designing stable control systems.
- Robotics for ensuring stability in motion planning.
- Network theory for analyzing the stability of distributed systems.

## Related Concepts
- [[Stability Theory]]
- [[Control Theory]]
- [[Nonlinear Dynamics]]
- [[Differential Equations]]

## Further Reading
- [[Lyapunov's Direct Method]]
- [[Asymptotic Stability]]
- [[Control Lyapunov Functions]]
