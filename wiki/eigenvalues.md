
# Eigenvalues

## Definition
In linear algebra, an [[eigenvalue]] is a scalar associated with a linear transformation represented by a square matrix. Given a square matrix \( A \in \mathbb{R}^{n \times n} \), a non-zero vector \( \mathbf{v} \in \mathbb{R}^n \) is called an [[eigenvector]] of \( A \) if it satisfies the equation:

\[
A \mathbf{v} = \lambda \mathbf{v}
\]

where \( \lambda \in \mathbb{R} \) is the eigenvalue corresponding to the eigenvector \( \mathbf{v} \).

## Characteristic Polynomial
To find the eigenvalues of a matrix \( A \), one typically computes the [[characteristic polynomial]], defined as:

\[
p(\lambda) = \det(A - \lambda I_n)
\]

where \( I_n \) is the identity matrix of size \( n \) and \( \det \) denotes the determinant. The eigenvalues are the roots of the characteristic polynomial \( p(\lambda) = 0 \).

## Properties
1. **Multiplicity**: Eigenvalues can have an associated [[algebraic multiplicity]], which is the number of times an eigenvalue appears as a root of the characteristic polynomial, and a [[geometric multiplicity]], which is the dimension of the eigenspace corresponding to that eigenvalue.

2. **Trace and Determinant**: The sum of the eigenvalues of a matrix \( A \) (counting algebraic multiplicities) is equal to the trace of \( A \), denoted as \( \text{tr}(A) \). The product of the eigenvalues is equal to the determinant of \( A \), denoted as \( \det(A) \).

3. **Diagonalization**: A matrix \( A \) is diagonalizable if there exists a matrix \( P \) such that:

\[
A = PDP^{-1}
\]

where \( D \) is a diagonal matrix containing the eigenvalues of \( A \). This is possible if and only if the algebraic multiplicity of each eigenvalue equals its geometric multiplicity.

## Applications
Eigenvalues have numerous applications across various fields, including:

- **Principal Component Analysis (PCA)**: In statistics, eigenvalues are used to determine the variance explained by each principal component.
- **Stability Analysis**: In control theory, the eigenvalues of a system's matrix can indicate the stability of the system.
- **Quantum Mechanics**: In physics, eigenvalues correspond to observable quantities, such as energy levels in quantum systems.

## Symbolic Notation
Let \( A \) be a square matrix of size \( n \). The eigenvalue equation can be expressed in a more compact form using the [[spectral theorem]]:

\[
A \mathbf{v} = \lambda \mathbf{v} \quad \text{for } \lambda \in \sigma(A)
\]

where \( \sigma(A) \) denotes the spectrum of \( A \), the set of all eigenvalues.

## Further Reading
- [[Spectral Theorem]]
- [[Matrix Diagonalization]]
- [[Characteristic Polynomial]]
- [[Eigenspace]]
- [[Principal Component Analysis]]
