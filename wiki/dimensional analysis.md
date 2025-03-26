
# [[Dimensional Analysis]]

## Overview
[[Dimensional Analysis]] is a mathematical technique used to analyze the relationships between physical quantities by identifying their fundamental dimensions. It is a powerful tool in both theoretical and applied physics, engineering, and applied mathematics, allowing for the simplification of complex problems and the derivation of relationships between variables.

## Fundamental Dimensions
In dimensional analysis, physical quantities are expressed in terms of fundamental dimensions, which typically include:
- **Length** \([L]\)
- **Mass** \([M]\)
- **Time** \([T]\)
- **Electric Current** \([I]\)
- **Temperature** \([Θ]\)
- **Amount of Substance** \([N]\)
- **Luminous Intensity** \([J]\)

Any physical quantity can be expressed as a product of these fundamental dimensions raised to appropriate powers. For example, the dimension of velocity \( v \) can be expressed as:

\[
[v] = [L][T]^{-1}
\]

## Dimensional Homogeneity
A key principle in dimensional analysis is that equations must be dimensionally homogeneous, meaning that all terms in an equation must have the same dimensional representation. This principle can be used to check the consistency of equations and to derive relationships between different physical quantities.

For instance, consider the equation for kinetic energy \( K \):

\[
K = \frac{1}{2} mv^2
\]

The dimensions of kinetic energy can be analyzed as follows:

\[
[K] = [M][L]^2[T]^{-2}
\]

This shows that the dimensions of kinetic energy are consistent with the dimensions of work, which is also expressed as force times distance.

## Buckingham π Theorem
The [[Buckingham π Theorem]] is a fundamental result in dimensional analysis that provides a systematic method for reducing the number of variables in a physical problem. It states that if a physical problem involves \( n \) variables and \( k \) fundamental dimensions, the problem can be reduced to \( n - k \) dimensionless parameters, known as π terms.

### Formulation
Let \( f \) be a function of \( n \) variables \( x_1, x_2, \ldots, x_n \) with dimensions \( [x_i] \). The relationship can be expressed as:

\[
f(x_1, x_2, \ldots, x_n) = 0
\]

Using the Buckingham π theorem, we can express this relationship in terms of \( n - k \) dimensionless groups \( π_1, π_2, \ldots, π_{n-k} \):

\[
f(π_1, π_2, \ldots, π_{n-k}) = 0
\]

### Example
Consider a problem involving the drag force \( F_d \) on a sphere moving through a fluid, which depends on the sphere's radius \( r \), the fluid's density \( ρ \), the fluid's viscosity \( μ \), and the velocity \( v \). The variables can be expressed in terms of their dimensions:

- \( [F_d] = [M][L][T]^{-2} \)
- \( [r] = [L] \)
- \( [ρ] = [M][L]^{-3} \)
- \( [μ] = [M][L]^{-1}[T]^{-1} \)
- \( [v] = [L][T]^{-1} \)

Applying the Buckingham π theorem, we can derive dimensionless groups such as the Reynolds number \( Re \):

\[
Re = \frac{ρvr}{μ}
\]

## Applications
Dimensional analysis has numerous applications, including:
- **Modeling and Simulation**: Simplifying complex physical models by reducing the number of variables.
- **Scaling Laws**: Deriving scaling relationships in fluid dynamics, thermodynamics, and other fields.
- **Experimental Design**: Guiding the design of experiments by identifying key dimensionless parameters.

## Limitations
While dimensional analysis is a powerful tool, it has limitations:
- It cannot provide specific numerical coefficients in relationships.
- It may not account for all physical phenomena, particularly in non-linear systems or when additional physical laws are involved.

## Conclusion
Dimensional analysis is an essential technique in the toolkit of scientists and engineers, providing insights into the relationships between physical quantities and facilitating the simplification of complex problems. Its principles, such as dimensional homogeneity and the Buckingham π theorem, enable the derivation of meaningful relationships that are crucial for both theoretical understanding and practical applications.

## References
- Buckingham, E. (1914). "On physically similar systems: Illustrations of the use of dimensional equations." *Physical Review*, 4(4), 345-376.
- Barenblatt, G. I. (1996). *Scaling, Self-Similarity, and Intermediate Asymptotics*. Cambridge University Press.
- Dimensional