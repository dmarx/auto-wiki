
# Central Limit Theorem

## Definition
The [[Central Limit Theorem]] (CLT) is a fundamental statistical theorem that states that, given a sufficiently large sample size, the distribution of the sample mean of a random variable will approximate a normal distribution, regardless of the original distribution of the variable. This theorem is crucial in the field of statistics as it justifies the use of the normal distribution in many practical applications.

## Mathematical Formulation
Let \( X_1, X_2, \ldots, X_n \) be a sequence of independent and identically distributed (i.i.d.) random variables, each with a mean \( \mu \) and a finite variance \( \sigma^2 \). The sample mean \( \bar{X} \) is defined as:

\[
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
\]

According to the Central Limit Theorem, as the sample size \( n \) approaches infinity, the distribution of the standardized sample mean approaches a standard normal distribution:

\[
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1)
\]

where \( Z \) is the standardized variable, \( \xrightarrow{d} \) denotes convergence in distribution, and \( N(0, 1) \) represents the standard normal distribution with mean 0 and variance 1.

## Conditions
The Central Limit Theorem holds under the following conditions:
1. The random variables \( X_i \) are independent.
2. The random variables \( X_i \) are identically distributed.
3. The mean \( \mu \) and variance \( \sigma^2 \) are finite.

## Applications
The Central Limit Theorem has numerous applications across various fields, including:
- **Statistical Inference**: It allows for the construction of confidence intervals and hypothesis testing using the normal distribution.
- **Quality Control**: In manufacturing, it helps in assessing the variability of product measurements.
- **Finance**: It is used in risk assessment and portfolio management, where the returns of assets can be modeled as random variables.

## Examples
1. **Dice Rolling**: Consider rolling a fair six-sided die multiple times. The mean of the outcomes will converge to a normal distribution as the number of rolls increases, even though the distribution of a single die roll is uniform.

2. **Sample Means**: If we take random samples of size \( n \) from a population with a known distribution (e.g., exponential, binomial), the distribution of the sample means will approach a normal distribution as \( n \) increases, regardless of the original distribution.

## Related Concepts
- [[Law of Large Numbers]]
- [[Normal Distribution]]
- [[Statistical Inference]]
- [[Sampling Distributions]]

## Further Reading
- [[Statistical Theory]]
- [[Applications of the Central Limit Theorem]]
- [[Convergence in Distribution]]
