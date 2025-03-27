
# State-Space Representation

[[State-Space Representation]] is a mathematical framework used to model dynamic systems in control theory and systems engineering. It provides a comprehensive way to describe the behavior of systems using state variables, which encapsulate all necessary information about the system's past behavior to predict its future behavior. This representation is particularly useful for analyzing and designing control systems.

## Mathematical Formulation

A state-space representation typically consists of two main equations: the state equation and the output equation.

### 1. State Equation

The state equation describes the evolution of the state vector \( \mathbf{x}(t) \) over time. It is generally expressed in the form:

\[
\frac{d\mathbf{x}(t)}{dt} = \mathbf{A} \mathbf{x}(t) + \mathbf{B} \mathbf{u}(t)
\]

where:
- \( \mathbf{x}(t) \in \mathbb{R}^n \) is the state vector at time \( t \),
- \( \mathbf{u}(t) \in \mathbb{R}^m \) is the input (control) vector,
- \( \mathbf{A} \in \mathbb{R}^{n \times n} \) is the state matrix that defines the system dynamics,
- \( \mathbf{B} \in \mathbb{R}^{n \times m} \) is the input matrix that defines how the input affects the state.

### 2. Output Equation

The output equation relates the state vector to the output vector \( \mathbf{y}(t) \):

\[
\mathbf{y}(t) = \mathbf{C} \mathbf{x}(t) + \mathbf{D} \mathbf{u}(t)
\]

where:
- \( \mathbf{y}(t) \in \mathbb{R}^p \) is the output vector,
- \( \mathbf{C} \in \mathbb{R}^{p \times n} \) is the output matrix that defines how the state contributes to the output,
- \( \mathbf{D} \in \mathbb{R}^{p \times m} \) is the feedthrough (or direct transmission) matrix that defines the direct effect of the input on the output.

## State-Space Representation in Discrete Time

In discrete-time systems, the state-space representation can be expressed as:

\[
\mathbf{x}[k+1] = \mathbf{A} \mathbf{x}[k] + \mathbf{B} \mathbf{u}[k]
\]

\[
\mathbf{y}[k] = \mathbf{C} \mathbf{x}[k] + \mathbf{D} \mathbf{u}[k]
\]

where \( k \) is the discrete time index.

## Properties of State-Space Systems

### 1. Controllability

A system is said to be controllable if it is possible to drive the state vector \( \mathbf{x}(t) \) to any desired state \( \mathbf{x}_d \) in a finite time using appropriate control inputs \( \mathbf{u}(t) \). The controllability matrix \( \mathbf{W_c} \) is defined as:

\[
\mathbf{W_c} = [\mathbf{B}, \mathbf{A} \mathbf{B}, \mathbf{A}^2 \mathbf{B}, \ldots, \mathbf{A}^{n-1} \mathbf{B}]
\]

The system is controllable if \( \text{rank}(\mathbf{W_c}) = n \).

### 2. Observability

A system is observable if the current state \( \mathbf{x}(t) \) can be determined from the output \( \mathbf{y}(t) \) over time. The observability matrix \( \mathbf{W_o} \) is defined as:

\[
\mathbf{W_o} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C} \mathbf{A} \\ \mathbf{C} \mathbf{A}^2 \\ \vdots \\ \mathbf{C} \mathbf{A}^{n-1} \end{bmatrix}
\]

The system is observable if \( \text{rank}(\mathbf{W_o}) = n \).

## Applications

State-space representation is widely used in various fields, including:

- **Control Systems**: Designing controllers for dynamic systems, such as PID controllers and state feedback controllers.
- **Signal Processing**: Modeling and analyzing systems for filtering and signal reconstruction.
- **Robotics**: Describing the dynamics of robotic systems for motion planning and control.
- **Economics**: Modeling economic systems and forecasting.

## Conclusion

State-space representation provides a powerful and flexible framework for modeling dynamic systems. By encapsulating the system's behavior in terms of state variables, it allows for comprehensive