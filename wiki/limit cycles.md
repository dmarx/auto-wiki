
# Limit Cycles

## Definition
A [[limit cycle]] is a closed trajectory in the phase space of a dynamical system that is isolated from other trajectories. It represents a periodic solution to a system of ordinary differential equations (ODEs) and is characterized by the property that nearby trajectories either converge to it or diverge from it over time. Formally, consider a dynamical system described by:

\[
\dot{x} = f(x)
\]

where \( x \in \mathbb{R}^n \) and \( f: \mathbb{R}^n \to \mathbb{R}^n \). A limit cycle \( \gamma \) is a periodic orbit such that there exists a neighborhood \( U \) of \( \gamma \) where:

- If \( x(0) \) is in \( U \) and \( x(0) \) is not on \( \gamma \), then \( x(t) \) approaches \( \gamma \) as \( t \to \infty \) (attracting limit cycle).
- If \( x(0) \) is in \( U \) and \( x(0) \) is on \( \gamma \), then \( x(t) \) remains on \( \gamma \) for all \( t \).

## Mathematical Characterization
Limit cycles can be analyzed using various methods, including:

1. **Poincaré-Bendixson Theorem**: This theorem states that in a two-dimensional autonomous system, if a trajectory does not converge to a fixed point, it must either approach a limit cycle or exhibit chaotic behavior.

2. **Bendixson-Dulac Criterion**: This criterion provides a method to determine the existence of limit cycles in planar systems. If there exists a continuously differentiable function \( \mu(x, y) \) such that the divergence of \( \mu f \) is non-zero, then the system does not have any limit cycles.

3. **Lyapunov Functions**: A Lyapunov function can also be used to analyze the stability of limit cycles. If a suitable Lyapunov function can be found that is positive definite and has a negative derivative along the trajectories, the limit cycle can be shown to be stable.

## Examples
1. **Van der Pol Oscillator**: The Van der Pol equation is a well-known example of a system exhibiting limit cycles:

\[
\dot{x} = y, \quad \dot{y} = \mu(1 - x^2)y - x
\]

where \( \mu > 0 \). This system has a unique limit cycle for \( \mu > 0 \) that attracts nearby trajectories.

2. **Simple Harmonic Oscillator**: The system described by:

\[
\dot{x} = -\omega^2 x
\]

has a limit cycle at the origin, but it is not isolated since all trajectories spiral into the origin. However, if we consider a perturbed system, such as:

\[
\dot{x} = -\omega^2 x + \epsilon \sin(\omega t)
\]

for small \( \epsilon \), the system can exhibit a limit cycle due to the periodic forcing.

## Applications
Limit cycles are significant in various fields, including:
- **Biology**: Modeling population dynamics where species exhibit periodic behavior.
- **Engineering**: Analyzing oscillations in control systems and circuits.
- **Physics**: Studying nonlinear oscillators and wave phenomena.

## Related Concepts
- [[Periodic Orbits]]
- [[Poincaré-Bendixson Theorem]]
- [[Nonlinear Dynamics]]
- [[Stability Theory]]

## Further Reading
- [[Van der Pol Oscillator]]
- [[Bendixson-Dulac Criterion]]
- [[Lyapunov Functions and Limit Cycles]]
