
# Eigenspace

## Overview
The [[eigenspace]] of a linear operator or matrix is a fundamental concept in linear algebra that describes the set of all eigenvectors associated with a particular eigenvalue, along with the zero vector. Eigenspaces play a crucial role in understanding the behavior of linear transformations, particularly in the context of diagonalization and spectral analysis.

## Mathematical Definition
Given a linear operator \( A: V \to V \) on a vector space \( V \), an eigenvalue \( \lambda \) is defined as a scalar such that there exists a non-zero vector \( \mathbf{v} \in V \) (the eigenvector) satisfying the equation:

\[
A \mathbf{v} = \lambda \mathbf{v}
\]

The eigenspace corresponding to the eigenvalue \( \lambda \), denoted as \( E_\lambda \), is defined as:

\[
E_\lambda = \{ \mathbf{v} \in V \mid A \mathbf{v} = \lambda \mathbf{v} \}
\]

This can also be expressed in terms of the null space of the operator \( A - \lambda I \):

\[
E_\lambda = \text{Null}(A - \lambda I)
\]

where \( I \) is the identity operator on \( V \).

## Properties of Eigenspaces
1. **Subspace**: The eigenspace \( E_\lambda \) is a subspace of the vector space \( V \). It contains the zero vector and is closed under vector addition and scalar multiplication.

2. **Dimension**: The dimension of the eigenspace \( E_\lambda \) is referred to as the geometric multiplicity of the eigenvalue \( \lambda \). It indicates the number of linearly independent eigenvectors associated with \( \lambda \).

3. **Multiplicity**: The algebraic multiplicity of an eigenvalue is the number of times it appears as a root of the characteristic polynomial of the matrix \( A \). The geometric multiplicity is always less than or equal to the algebraic multiplicity.

## Example
Consider the matrix \( A \):

\[
A = \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}
\]

To find the eigenvalues, we solve the characteristic polynomial:

\[
\det(A - \lambda I) = 0
\]

Calculating this gives:

\[
\det\begin{pmatrix}
4 - \lambda & 1 \\
2 & 3 - \lambda
\end{pmatrix} = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0
\]

The eigenvalues are \( \lambda_1 = 5 \) and \( \lambda_2 = 2 \).

### Eigenspaces
1. For \( \lambda_1 = 5 \):

\[
A - 5I = \begin{pmatrix}
-1 & 1 \\
2 & -2
\end{pmatrix}
\]

The corresponding eigenspace is found by solving:

\[
\begin{pmatrix}
-1 & 1 \\
2 & -2
\end{pmatrix} \begin{pmatrix}
x_1 \\
x_2
\end{pmatrix} = \begin{pmatrix}
0 \\
0
\end{pmatrix}
\]

This leads to the equation \( x_1 = x_2 \), so the eigenspace is:

\[
E_5 = \text{span}\left\{ \begin{pmatrix}
1 \\
1
\end{pmatrix} \right\}
\]

2. For \( \lambda_2 = 2 \):

\[
A - 2I = \begin{pmatrix}
2 & 1 \\
2 & 1
\end{pmatrix}
\]

The corresponding eigenspace is found similarly, leading to:

\[
E_2 = \text{span}\left\{ \begin{pmatrix}
-1 \\
2
\end{pmatrix} \right\}
\]

## Applications
Eigenspaces are widely used in various fields, including:
- [[Principal Component Analysis (PCA)]]: Where eigenspaces of the covariance matrix are used to identify principal components.
- [[Quantum Mechanics]]: Where observables are represented by operators, and their eigenvalues correspond to measurable quantities.
- [[Differential Equations]]: In solving systems of linear differential equations, where the eigenvalues and eigenvectors determine the behavior of solutions.

## Conclusion
The concept of eigenspaces is central to the study of linear transformations and matrices. Understanding eigenspaces allows for deeper insights into the structure of linear operators, facilitating applications across mathematics, physics, and engineering.

## References