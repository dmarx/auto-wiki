
# Linear Algebra

## Overview
Linear Algebra is a branch of mathematics that deals with vector spaces and linear mappings between these spaces. It is foundational for various fields, including [[computer science]], [[engineering]], [[physics]], and [[economics]]. The study of linear algebra involves the analysis of systems of linear equations, matrices, determinants, eigenvalues, and eigenvectors, among other concepts.

## Fundamental Concepts

### Vectors
A vector is an element of a vector space, which can be represented as an ordered list of numbers. In \( n \)-dimensional space, a vector \( \mathbf{v} \) can be expressed as:

\[
\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}
\]

Vectors can be added together and multiplied by scalars, following the rules of vector addition and scalar multiplication.

### Matrices
A matrix is a rectangular array of numbers arranged in rows and columns. An \( m \times n \) matrix \( \mathbf{A} \) can be represented as:

\[
\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}
\]

Matrices can be added, multiplied, and transformed, and they play a crucial role in representing linear transformations.

### Linear Transformations
A linear transformation \( T: \mathbb{R}^n \to \mathbb{R}^m \) is a function that maps vectors from one vector space to another while preserving the operations of vector addition and scalar multiplication. Mathematically, this can be expressed as:

\[
T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}), \quad T(c\mathbf{u}) = cT(\mathbf{u})
\]

for all vectors \( \mathbf{u}, \mathbf{v} \) in \( \mathbb{R}^n \) and scalar \( c \).

### Systems of Linear Equations
A system of linear equations can be represented in matrix form as:

\[
\mathbf{A} \mathbf{x} = \mathbf{b}
\]

where \( \mathbf{A} \) is a matrix of coefficients, \( \mathbf{x} \) is a vector of variables, and \( \mathbf{b} \) is a vector of constants. The solution to this system can be found using various methods, including:

- **Gaussian Elimination**: A systematic method for solving linear systems by transforming the matrix into row echelon form.
- **Matrix Inversion**: If \( \mathbf{A} \) is invertible, the solution can be expressed as \( \mathbf{x} = \mathbf{A}^{-1} \mathbf{b} \).

### Determinants
The determinant is a scalar value that can be computed from a square matrix and provides important information about the matrix, such as whether it is invertible. For a \( 2 \times 2 \) matrix \( \mathbf{A} \):

\[
\text{det}(\mathbf{A}) = a_{11}a_{22} - a_{12}a_{21}
\]

For larger matrices, determinants can be computed using various methods, including cofactor expansion and row reduction.

### Eigenvalues and Eigenvectors
An eigenvalue \( \lambda \) and its corresponding eigenvector \( \mathbf{v} \) of a matrix \( \mathbf{A} \) satisfy the equation:

\[
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}
\]

Eigenvalues provide insight into the properties of linear transformations, such as stability and oscillatory behavior. The characteristic polynomial, given by:

\[
\text{det}(\mathbf{A} - \lambda \mathbf{I}) = 0
\]

is used to find the eigenvalues, where \( \mathbf{I} \) is the identity matrix.

## Applications
Linear algebra is widely used in various fields, including:

- **Computer Graphics**: Transformations and projections of images.
- **Machine Learning**: Data representation, dimensionality reduction (e.g., [[Principal Component Analysis]]), and optimization.
- **Physics**: Quantum mechanics and the study of linear systems.
- **Economics**: Input-output models and optimization problems.

## Mathematical Formalism
The mathematical framework of linear algebra employs the following notations:

- **Vector Spaces**: Denoted as \( V \), a set of vectors that can be