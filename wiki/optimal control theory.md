
# Optimal Control Theory

## Definition
**Optimal Control Theory** is a mathematical framework for determining control policies that will minimize (or maximize) a certain performance criterion over time. It is widely used in various fields such as engineering, economics, and robotics, where systems are governed by dynamic equations and require optimal decision-making to achieve desired outcomes.

## Mathematical Formulation
The fundamental problem in optimal control theory can be expressed as follows:

Given a dynamic system described by the state equation:

\[
\dot{x}(t) = f(x(t), u(t), t)
\]

where:
- \( x(t) \in \mathbb{R}^n \) is the state vector at time \( t \),
- \( u(t) \in \mathbb{R}^m \) is the control input,
- \( f \) is a function that describes the system dynamics.

The objective is to find a control policy \( u(t) \) that minimizes a cost functional \( J \):

\[
J = \int_{t_0}^{t_f} L(x(t), u(t), t) \, dt + \Phi(x(t_f))
\]

where:
- \( L(x(t), u(t), t) \) is the running cost (or stage cost),
- \( \Phi(x(t_f)) \) is the terminal cost at the final time \( t_f \),
- \( t_0 \) is the initial time.

## Types of Optimal Control Problems
1. **Linear Quadratic Regulator (LQR)**: A special case where the system dynamics are linear, and the cost functional is quadratic in both state and control variables. The LQR problem can be formulated as:

\[
\dot{x}(t) = Ax(t) + Bu(t)
\]

with the cost functional:

\[
J = \int_{t_0}^{t_f} (x(t)^T Q x(t) + u(t)^T R u(t)) \, dt
\]

where \( Q \) and \( R \) are positive semi-definite matrices.

2. **Nonlinear Control**: Involves systems where the dynamics \( f \) are nonlinear. Techniques such as the **Pontryagin's Maximum Principle** and **Dynamic Programming** are often employed to solve these problems.

3. **Stochastic Control**: Deals with systems that are influenced by random disturbances. The objective is to minimize the expected cost, leading to formulations that incorporate probabilistic models.

## Pontryagin's Maximum Principle
The **Pontryagin's Maximum Principle** provides necessary conditions for optimality in control problems. It introduces the Hamiltonian function \( H \):

\[
H(x, u, \lambda, t) = L(x, u, t) + \lambda^T f(x, u, t)
\]

where \( \lambda \) is the costate vector. The necessary conditions for optimal control are:

1. The state dynamics must satisfy the state equation.
2. The costate dynamics are given by:

\[
\dot{\lambda}(t) = -\frac{\partial H}{\partial x}
\]

3. The control must maximize the Hamiltonian:

\[
u^*(t) = \arg \max_{u} H(x(t), u, \lambda(t), t)
\]

## Applications
- **Engineering**: Optimal control is used in the design of control systems for aircraft, spacecraft, and industrial processes.
- **Economics**: It is applied in resource management, investment strategies, and economic policy formulation.
- **Robotics**: Optimal control techniques are employed for trajectory planning and motion control of robotic systems.

## Numerical Methods
Solving optimal control problems analytically can be challenging, especially for nonlinear systems. Numerical methods such as:
- **Direct Methods**: These involve discretizing the control and state trajectories and solving the resulting finite-dimensional optimization problem.
- **Indirect Methods**: These utilize the Pontryagin's Maximum Principle to derive necessary conditions and solve the resulting boundary value problem.

## Related Concepts
- [[Dynamic Programming]]
- [[Hamiltonian Mechanics]]
- [[Linear Quadratic Regulator]]
- [[Stochastic Control]]
- [[Feedback Control Systems]]
- [[State-Space Representation]]
