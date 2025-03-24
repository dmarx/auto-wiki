
# Linear Programming

## Definition
[[Linear programming]] (LP) is a mathematical method for determining a way to achieve the best outcome in a given mathematical model. Its function is to maximize or minimize a linear objective function, subject to a set of linear equality and inequality constraints. Linear programming is widely used in various fields such as economics, business, engineering, and military applications.

## Mathematical Formulation
A linear programming problem can be formulated as follows:

### Objective Function
The objective function is a linear function that needs to be maximized or minimized:
\[
\text{Maximize (or Minimize) } z = c^T x
\]
where:
- \( z \) is the objective value.
- \( c \) is a vector of coefficients.
- \( x \) is a vector of decision variables.

### Constraints
The constraints are linear equations or inequalities that restrict the values of the decision variables:
\[
Ax \leq b
\]
\[
x \geq 0
\]
where:
- \( A \) is a matrix of coefficients.
- \( b \) is a vector of constants.
- \( x \) is the vector of decision variables, which must be non-negative.

## Graphical Representation
In two dimensions, linear programming problems can be visualized graphically. The feasible region, defined by the constraints, is a convex polygon. The optimal solution lies at one of the vertices of this polygon, according to the Fundamental Theorem of Linear Programming.

## Simplex Method
The [[Simplex method]] is one of the most widely used algorithms for solving linear programming problems. It operates on the vertices of the feasible region and iteratively moves towards the optimal vertex.

### Steps of the Simplex Method:
1. **Initialization**: Start at a basic feasible solution.
2. **Pivoting**: Identify the entering and leaving variables to move to an adjacent vertex.
3. **Iteration**: Repeat the pivoting process until no further improvements can be made to the objective function.

The Simplex method is efficient and can solve large-scale linear programming problems.

## Duality
Every linear programming problem has an associated dual problem. The dual provides insights into the original problem and can be used to derive bounds on the optimal value. If the primal problem is defined as:

\[
\text{Maximize } z = c^T x \quad \text{subject to } Ax \leq b, \, x \geq 0
\]

The dual problem is formulated as:

\[
\text{Minimize } w = b^T y \quad \text{subject to } A^T y \geq c
\]

where \( y \) is the vector of dual variables.

## Applications
Linear programming has a wide range of applications, including:

- **Resource Allocation**: Optimizing the allocation of limited resources among competing activities.
- **Production Planning**: Determining the optimal mix of products to manufacture.
- **Transportation Problems**: Minimizing transportation costs while meeting supply and demand constraints.
- **Network Flow Problems**: Optimizing flow through a network.

## Conclusion
Linear programming is a powerful optimization technique that provides a systematic approach to decision-making in various fields. Its ability to model complex problems with linear relationships makes it an essential tool for researchers and practitioners alike.

[[Simplex method]] | [[dual problem]] | [[convex optimization]] | [[resource allocation]] | [[transportation problem]]
