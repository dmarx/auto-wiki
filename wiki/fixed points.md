
# Fixed Points

In mathematics, a [[fixed point]] is a point that is invariant under a given function or transformation. More formally, if \( f: X \to X \) is a function mapping a set \( X \) to itself, then a point \( x^* \in X \) is called a fixed point of \( f \) if:

\[
f(x^*) = x^*
\]

Fixed points are significant in various fields, including analysis, topology, and dynamical systems, as they often represent equilibrium states or stable configurations of a system.

## Types of Fixed Points

1. **Attractive Fixed Points**: A fixed point \( x^* \) is attractive if, for points \( x \) sufficiently close to \( x^* \), the iterates of \( f \) converge to \( x^* \). Mathematically, this can be expressed as:

\[
\lim_{n \to \infty} f^n(x) = x^* \quad \text{for } x \text{ near } x^*
\]

where \( f^n \) denotes the \( n \)-th iterate of \( f \).

2. **Repulsive Fixed Points**: A fixed point is repulsive if points near \( x^* \) move away from it under iteration. This can be expressed as:

\[
\lim_{n \to \infty} f^n(x) \neq x^* \quad \text{for } x \text{ near } x^*
\]

3. **Neutral Fixed Points**: A fixed point is neutral if the behavior of points near it does not lead to convergence or divergence, often requiring further analysis to determine stability.

## Existence of Fixed Points

The existence of fixed points is guaranteed by several important theorems:

1. **Brouwer Fixed Point Theorem**: This theorem states that any continuous function mapping a compact convex set to itself has at least one fixed point. For example, any continuous function from a closed disk in \( \mathbb{R}^n \) to itself has a fixed point.

2. **Banach Fixed Point Theorem**: Also known as the contraction mapping theorem, it states that if \( f \) is a contraction mapping on a complete metric space, then \( f \) has a unique fixed point. A function \( f \) is a contraction if there exists a constant \( 0 \leq k < 1 \) such that:

\[
d(f(x), f(y)) \leq k \cdot d(x, y) \quad \text{for all } x, y
\]

where \( d \) is a metric on the space.

## Applications

Fixed points have numerous applications across various fields:

1. **Dynamical Systems**: In the study of dynamical systems, fixed points represent equilibrium states. The stability of these points can determine the long-term behavior of the system.

2. **Economics**: In economic models, fixed points can represent equilibria in supply and demand, where the quantity supplied equals the quantity demanded.

3. **Computer Science**: Fixed points are used in the semantics of programming languages, particularly in defining recursive functions and in the analysis of algorithms.

4. **Numerical Methods**: Fixed-point iteration is a method for finding solutions to equations of the form \( x = f(x) \). This method involves iteratively applying \( f \) starting from an initial guess until convergence to a fixed point is achieved.

## Conclusion

Fixed points are a fundamental concept in mathematics with wide-ranging implications in various disciplines. Understanding their properties and the conditions under which they exist is crucial for analyzing the behavior of functions and systems.

[[Brouwer Fixed Point Theorem]] | [[Banach Fixed Point Theorem]] | [[Dynamical Systems]] | [[Fixed-Point Iteration]]
