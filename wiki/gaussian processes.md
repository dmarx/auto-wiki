
# Gaussian Processes

## Overview
A [[Gaussian process]] (GP) is a collection of random variables, any finite number of which have a joint Gaussian distribution. GPs are a powerful tool in [[machine learning]] and [[statistical modeling]], particularly for regression and classification tasks. They provide a non-parametric approach to modeling functions, allowing for flexible representations of uncertainty in predictions.

## Mathematical Formulation
A Gaussian process is fully specified by its mean function \( m(x) \) and covariance function (or kernel) \( k(x, x') \):

\[
m(x) = \mathbb{E}[f(x)]
\]

\[
k(x, x') = \text{Cov}(f(x), f(x'))
\]

where:
- \( f(x) \) is the function being modeled,
- \( x \) and \( x' \) are input points in the input space.

The mean function \( m(x) \) is often assumed to be zero for simplicity, leading to the formulation:

\[
f(x) \sim \mathcal{GP}(m(x), k(x, x'))
\]

## Covariance Functions
The choice of covariance function \( k(x, x') \) is crucial as it encodes assumptions about the function's smoothness, periodicity, and other properties. Commonly used kernels include:

### 1. Squared Exponential Kernel
The squared exponential (or radial basis function) kernel is defined as:

\[
k(x, x') = \sigma_f^2 \exp\left(-\frac{(x - x')^2}{2\ell^2}\right)
\]

where:
- \( \sigma_f^2 \) is the variance,
- \( \ell \) is the length scale.

### 2. Matérn Kernel
The Matérn kernel is a generalization that introduces a parameter \( \nu \) to control the smoothness of the function:

\[
k(x, x') = \frac{2^{1 - \nu}}{\Gamma(\nu)} \left(\frac{\sqrt{2\nu} |x - x'|}{\ell}\right)^\nu K_\nu\left(\frac{\sqrt{2\nu} |x - x'|}{\ell}\right)
\]

where \( K_\nu \) is the modified Bessel function of the second kind.

## Inference with Gaussian Processes
Given a set of training data \( \mathbf{X} = \{x_1, x_2, \ldots, x_n\} \) and corresponding outputs \( \mathbf{y} = \{y_1, y_2, \ldots, y_n\} \), the joint distribution of the observed outputs and the function values at new inputs \( \mathbf{X_*} \) can be expressed as:

\[
\begin{bmatrix}
\mathbf{y} \\
\mathbf{f_*}
\end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix}
m(\mathbf{X}) \\
m(\mathbf{X_*})
\end{bmatrix}, \begin{bmatrix}
K(\mathbf{X}, \mathbf{X}) & K(\mathbf{X}, \mathbf{X_*}) \\
K(\mathbf{X_*}, \mathbf{X}) & K(\mathbf{X_*}, \mathbf{X_*})
\end{bmatrix}\right)
\]

where:
- \( K(\mathbf{X}, \mathbf{X}) \) is the covariance matrix of the training inputs,
- \( K(\mathbf{X}, \mathbf{X_*}) \) is the covariance between training and test inputs,
- \( K(\mathbf{X_*}, \mathbf{X_*}) \) is the covariance matrix of the test inputs.

### Posterior Distribution
The posterior distribution of the function values at the new inputs \( \mathbf{f_*} \) given the observed data can be derived using properties of multivariate Gaussian distributions:

\[
\mathbf{f_*} | \mathbf{X}, \mathbf{y}, \mathbf{X_*} \sim \mathcal{N}(\mathbf{\mu_*}, \mathbf{\Sigma_*})
\]

where:
- The mean \( \mathbf{\mu_*} \) is given by:

\[
\mathbf{\mu_*} = K(\mathbf{X_*}, \mathbf{X}) K(\mathbf{X}, \mathbf{X})^{-1} \mathbf{y}
\]

- The covariance \( \mathbf{\Sigma_*} \) is given by:

\[
\mathbf{\Sigma_*} = K(\mathbf{X_*}, \mathbf{X_*}) - K(\mathbf{X_*}, \mathbf{X}) K(\mathbf{X}, \mathbf{X})^{-1} K(\mathbf{X}, \mathbf