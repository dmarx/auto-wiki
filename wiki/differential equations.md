
# Differential Equations

## Definition
A [[differential equation]] is a mathematical equation that relates a function with its derivatives. These equations describe various phenomena in fields such as physics, engineering, biology, and economics, where the rate of change of a quantity is related to the quantity itself. Differential equations can be classified into several categories based on their characteristics.

## Types of Differential Equations

### 1. Ordinary Differential Equations (ODEs)
An ordinary differential equation involves functions of a single variable and their derivatives. The general form of an ODE is:

\[
F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \ldots, \frac{d^n y}{dx^n}\right) = 0
\]

where \( y = y(x) \) is the unknown function, and \( n \) is the order of the differential equation.

#### Example
A first-order linear ODE can be expressed as:

\[
\frac{dy}{dx} + P(x)y = Q(x)
\]

where \( P(x) \) and \( Q(x) \) are continuous functions.

### 2. Partial Differential Equations (PDEs)
Partial differential equations involve functions of multiple variables and their partial derivatives. The general form of a PDE is:

\[
F\left(x_1, x_2, \ldots, x_n, u, \frac{\partial u}{\partial x_1}, \frac{\partial u}{\partial x_2}, \ldots, \frac{\partial^m u}{\partial x_1^{k_1} \partial x_2^{k_2} \ldots \partial x_n^{k_n}}\right) = 0
\]

where \( u = u(x_1, x_2, \ldots, x_n) \) is the unknown function.

#### Example
The heat equation, a second-order PDE, is given by:

\[
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
\]

where \( \alpha \) is the thermal diffusivity, and \( \nabla^2 \) is the Laplacian operator.

## Solutions of Differential Equations

### General Solution
The general solution of a differential equation includes all possible solutions and contains arbitrary constants. For example, the general solution of the first-order linear ODE:

\[
\frac{dy}{dx} + P(x)y = Q(x)
\]

can be found using an integrating factor \( \mu(x) = e^{\int P(x) \, dx} \):

\[
y(x) = \frac{1}{\mu(x)}\left(\int Q(x)\mu(x) \, dx + C\right)
\]

where \( C \) is an arbitrary constant.

### Particular Solution
A particular solution is a specific solution that satisfies the differential equation and any initial or boundary conditions.

## Applications
Differential equations are used to model a wide range of phenomena, including:
- **Physics**: Describing motion, heat transfer, and wave propagation.
- **Biology**: Modeling population dynamics and the spread of diseases.
- **Economics**: Analyzing growth models and market dynamics.

## Related Concepts
- [[Initial Value Problem]]
- [[Boundary Value Problem]]
- [[Stability Analysis]]
- [[Numerical Methods for Differential Equations]]

## Further Reading
- [[Ordinary Differential Equations]]
- [[Partial Differential Equations]]
- [[Laplace Transforms]]
- [[Fourier Series and Differential Equations]]
