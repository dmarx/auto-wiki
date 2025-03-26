
# Principal Component Analysis

## Overview
[[Principal Component Analysis]] (PCA) is a statistical technique used for dimensionality reduction while preserving as much variance as possible in high-dimensional datasets. It transforms the original variables into a new set of uncorrelated variables called principal components, which are ordered by the amount of variance they capture from the data. PCA is widely used in fields such as machine learning, image processing, and exploratory data analysis.

## Mathematical Formulation

### Data Representation
Consider a dataset represented as a matrix \( X \in \mathbb{R}^{n \times p} \), where \( n \) is the number of observations and \( p \) is the number of variables. Each row corresponds to an observation, and each column corresponds to a variable.

### Centering the Data
Before applying PCA, the data should be centered by subtracting the mean of each variable:

\[
X_{centered} = X - \bar{X}
\]

where \( \bar{X} \) is the mean vector of the dataset.

### Covariance Matrix
The covariance matrix \( C \) of the centered data is computed as:

\[
C = \frac{1}{n-1} X_{centered}^T X_{centered}
\]

This matrix captures the relationships between the variables, with each element \( C_{ij} \) representing the covariance between variables \( i \) and \( j \).

### Eigenvalue Decomposition
To find the principal components, we perform an eigenvalue decomposition of the covariance matrix:

\[
C v = \lambda v
\]

where \( \lambda \) are the eigenvalues and \( v \) are the corresponding eigenvectors. The eigenvalues indicate the amount of variance captured by each principal component.

### Principal Components
The principal components are obtained by projecting the original data onto the eigenvectors corresponding to the largest eigenvalues. If \( V \) is the matrix of eigenvectors, the principal components \( Z \) can be expressed as:

\[
Z = X_{centered} V_k
\]

where \( V_k \) contains the top \( k \) eigenvectors corresponding to the largest \( k \) eigenvalues.

## Properties of PCA

### Variance Explained
The proportion of variance explained by each principal component can be calculated as:

\[
\text{Variance}_{PC_i} = \frac{\lambda_i}{\sum_{j=1}^{p} \lambda_j}
\]

where \( \lambda_i \) is the \( i \)-th eigenvalue. This helps in determining how many principal components to retain for analysis.

### Orthogonality
The principal components are orthogonal to each other, meaning that they are uncorrelated. This property simplifies the analysis and interpretation of the transformed data.

## Applications

### Dimensionality Reduction
PCA is commonly used to reduce the dimensionality of datasets while retaining the most important features. This is particularly useful in preprocessing data for machine learning algorithms, where high-dimensional data can lead to overfitting.

### Data Visualization
By projecting high-dimensional data onto two or three principal components, PCA facilitates visualization, allowing researchers to identify patterns, clusters, and outliers in the data.

### Noise Reduction
PCA can help in denoising data by retaining only the principal components that capture the most variance, effectively filtering out noise associated with lower-variance components.

## Limitations

### Linearity
PCA assumes linear relationships among variables, which may not capture complex structures in the data. For nonlinear dimensionality reduction, techniques such as [[t-distributed Stochastic Neighbor Embedding]] (t-SNE) or [[Kernel PCA]] may be more appropriate.

### Sensitivity to Scaling
PCA is sensitive to the scale of the data. It is essential to standardize the data (e.g., using z-scores) before applying PCA, especially when variables are measured on different scales.

## Conclusion
Principal Component Analysis is a powerful tool for dimensionality reduction and data analysis, providing insights into the structure of high-dimensional datasets. Its mathematical foundation and practical applications make it a fundamental technique in statistics and machine learning.

## References
- [[Dimensionality Reduction]]
- [[t-distributed Stochastic Neighbor Embedding]]
- [[Kernel PCA]]
- [[Eigenvalue Decomposition]]
