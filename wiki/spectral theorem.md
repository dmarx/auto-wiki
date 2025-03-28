
# Spectral Theorem

## Overview
The [[spectral theorem]] is a fundamental result in linear algebra and functional analysis that characterizes the structure of linear operators on finite-dimensional and infinite-dimensional vector spaces. It provides a powerful framework for understanding the eigenvalues and eigenvectors of operators, particularly in the context of self-adjoint (or Hermitian) operators in Hilbert spaces.

## Mathematical Formulation

### Finite-Dimensional Case
For a finite-dimensional vector space \( V \) with an inner product, the spectral theorem states that any self-adjoint operator \( A: V \to V \) can be diagonalized. Specifically, there exists an orthonormal basis of \( V \) consisting of eigenvectors of \( A \). If \( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \) are the eigenvectors corresponding to the eigenvalues \( \{ \lambda_1, \lambda_2, \ldots, \lambda_n \} \), then:

\[
A \mathbf{v}_i = \lambda_i \mathbf{v}_i \quad \text{for } i = 1, 2, \ldots, n
\]

The operator can be expressed in terms of its eigenvalues and eigenvectors as:

\[
A = \sum_{i=1}^{n} \lambda_i \mathbf{v}_i \mathbf{v}_i^*
\]

where \( \mathbf{v}_i^* \) denotes the conjugate transpose of \( \mathbf{v}_i \).

### Infinite-Dimensional Case
In the context of Hilbert spaces, the spectral theorem extends to bounded self-adjoint operators. If \( A \) is a bounded self-adjoint operator on a Hilbert space \( \mathcal{H} \), then there exists a spectral measure \( E \) such that:

\[
A = \int_{\sigma(A)} \lambda \, dE(\lambda)
\]

where \( \sigma(A) \) is the spectrum of \( A \). The spectral measure \( E \) assigns a projection operator \( E(B) \) to each Borel set \( B \subseteq \sigma(A) \), allowing for the decomposition of the operator into its spectral components.

## Eigenvalues and Eigenvectors
The eigenvalues of a self-adjoint operator are real, and the corresponding eigenvectors associated with distinct eigenvalues are orthogonal. This property is crucial for applications in quantum mechanics and other fields where orthogonality and completeness of eigenstates are essential.

### Example: Matrix Representation
Consider a self-adjoint matrix \( A \):

\[
A = \begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
\]

To find the eigenvalues, we solve the characteristic polynomial:

\[
\det(A - \lambda I) = 0
\]

Calculating this gives:

\[
\det\begin{pmatrix}
2 - \lambda & 1 \\
1 & 2 - \lambda
\end{pmatrix} = (2 - \lambda)^2 - 1 = 0
\]

The eigenvalues are \( \lambda_1 = 3 \) and \( \lambda_2 = 1 \). The corresponding eigenvectors can be found by solving \( (A - \lambda I) \mathbf{v} = 0 \).

## Applications
The spectral theorem has numerous applications across various fields, including:
- [[Quantum Mechanics]]: Where observables are represented by self-adjoint operators, and measurements correspond to eigenvalues.
- [[Principal Component Analysis (PCA)]]: In statistics, where the covariance matrix is diagonalized to identify principal components.
- [[Control Theory]]: For analyzing the stability of systems through eigenvalue analysis.

## Conclusion
The spectral theorem is a cornerstone of linear algebra and functional analysis, providing deep insights into the structure of linear operators. Its implications extend across mathematics, physics, and engineering, making it an essential tool for both theoretical and applied disciplines.

## References
- [[Linear Algebra]]
- [[Functional Analysis]]
- [[Eigenvalues and Eigenvectors]]
- [[Self-Adjoint Operators]]
