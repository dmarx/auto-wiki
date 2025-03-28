
# Latent Variable Models

## Overview
[[Latent variable models]] (LVMs) are statistical models that assume the existence of unobserved (latent) variables that influence observed data. These models are particularly useful in situations where the underlying structure of the data is not directly observable, allowing for the modeling of complex phenomena in fields such as psychology, economics, and machine learning.

## Mathematical Formulation
A latent variable model can be expressed in terms of a joint distribution of observed variables \( \mathbf{Y} \) and latent variables \( \mathbf{Z} \). The relationship can be formalized as:

\[
p(\mathbf{Y}, \mathbf{Z}) = p(\mathbf{Y} | \mathbf{Z}) p(\mathbf{Z})
\]

where:
- \( p(\mathbf{Y} | \mathbf{Z}) \) is the conditional distribution of the observed variables given the latent variables,
- \( p(\mathbf{Z}) \) is the prior distribution of the latent variables.

### Example: Factor Analysis
In [[factor analysis]], the observed variables \( \mathbf{Y} \) can be modeled as a linear combination of latent factors \( \mathbf{F} \) plus noise:

\[
\mathbf{Y} = \mathbf{A} \mathbf{F} + \mathbf{\epsilon}
\]

where:
- \( \mathbf{A} \) is the factor loading matrix,
- \( \mathbf{\epsilon} \) is the error term, typically assumed to be normally distributed.

## Inference in Latent Variable Models
Inference in LVMs often involves estimating the parameters of the model and inferring the latent variables. This can be achieved through methods such as:

### Expectation-Maximization (EM) Algorithm
The EM algorithm is a popular method for maximum likelihood estimation in models with latent variables. It consists of two steps:
1. **Expectation Step (E-step)**: Compute the expected value of the log-likelihood function, given the current estimates of the parameters.
2. **Maximization Step (M-step)**: Update the parameters by maximizing the expected log-likelihood obtained in the E-step.

Mathematically, the E-step can be expressed as:

\[
Q(\theta | \theta^{(t)}) = \mathbb{E}_{\mathbf{Z} | \mathbf{Y}, \theta^{(t)}} [\log p(\mathbf{Y}, \mathbf{Z} | \theta)]
\]

where \( \theta^{(t)} \) are the current parameter estimates.

## Types of Latent Variable Models
Latent variable models can be categorized into several types, including:

### 1. Gaussian Mixture Models (GMM)
GMMs assume that the observed data is generated from a mixture of several Gaussian distributions, each associated with a latent variable representing the cluster membership. The model can be expressed as:

\[
p(\mathbf{Y}) = \sum_{k=1}^{K} \pi_k \mathcal{N}(\mathbf{Y} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)
\]

where:
- \( \pi_k \) is the mixing coefficient for component \( k \),
- \( \mathcal{N}(\mathbf{Y} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k) \) is the Gaussian distribution with mean \( \boldsymbol{\mu}_k \) and covariance \( \boldsymbol{\Sigma}_k \).

### 2. Hidden Markov Models (HMM)
HMMs are used for modeling time series data where the system is assumed to be a Markov process with unobserved states. The model is characterized by:

\[
p(\mathbf{Y} | \mathbf{Z}) = \prod_{t=1}^{T} p(y_t | z_t)
\]

where \( z_t \) represents the hidden state at time \( t \).

### 3. Structural Equation Models (SEM)
SEMs extend traditional regression models by incorporating latent variables and specifying relationships among them. The structural equations can be represented as:

\[
\mathbf{Y} = \mathbf{B} \mathbf{Y} + \mathbf{\Gamma} \mathbf{X} + \mathbf{\epsilon}
\]

where \( \mathbf{B} \) represents the coefficients of the endogenous variables, \( \mathbf{\Gamma} \) represents the coefficients of the exogenous variables \( \mathbf{X} \), and \( \mathbf{\epsilon} \) is the error term.

## Applications
Latent variable models are widely used in various domains, including:
- [[Psychometrics]]: For modeling psychological traits that are not directly observable.
- [[Econometrics]]: For modeling economic indicators influenced by unobserved factors.
- [[Machine Learning]]: In applications such as topic modeling (e.g., [[Latent Dirich