
# Complexity Theory

## Definition
[[Complexity Theory]] is a branch of theoretical computer science that studies the resources required to solve computational problems. It primarily focuses on classifying problems based on their inherent difficulty and the efficiency of algorithms that solve them. The main resources of interest are time and space, which correspond to the amount of computational time and memory required by an algorithm.

## Key Concepts

### 1. Computational Complexity
Computational complexity is concerned with the classification of problems based on the resources needed to solve them. Problems are typically categorized into complexity classes, which are defined by the type of resources required.

#### Complexity Classes
- **P**: The class of decision problems that can be solved by a deterministic Turing machine in polynomial time. Formally, a problem \( L \) is in P if there exists an algorithm that decides \( L \) in time \( O(n^k) \) for some constant \( k \), where \( n \) is the size of the input.
  
- **NP**: The class of decision problems for which a given solution can be verified in polynomial time by a deterministic Turing machine. A problem \( L \) is in NP if there exists a polynomial-time verifier \( V \) such that for any instance \( x \) of \( L \):
  
  \[
  x \in L \implies \exists y \text{ such that } V(x, y) = \text{true}
  \]

- **NP-Complete**: A subset of NP problems that are at least as hard as the hardest problems in NP. A problem \( L \) is NP-complete if:
  1. \( L \) is in NP.
  2. Every problem \( L' \) in NP can be reduced to \( L \) in polynomial time.

- **NP-Hard**: A class of problems that are at least as hard as the hardest problems in NP, but are not necessarily in NP themselves. NP-hard problems may not have a decision version.

### 2. Reductions
Reductions are a fundamental concept in complexity theory used to show the relationship between problems. A problem \( A \) can be reduced to problem \( B \) if an algorithm for \( B \) can be used to solve \( A \) in polynomial time. This is often denoted as \( A \leq_p B \).

### 3. Hierarchy Theorems
Hierarchy theorems provide insights into the relationships between different complexity classes. For example, the time hierarchy theorem states that for any function \( f(n) \) that grows faster than any polynomial, there exists a language that can be decided in time \( O(f(n)) \) but not in time \( O(n^k) \) for any constant \( k \).

## Applications
Complexity theory has significant implications in various fields, including:
- **Cryptography**: Many cryptographic protocols rely on the hardness of certain NP-complete problems.
- **Algorithm Design**: Understanding the complexity of problems helps in designing efficient algorithms.
- **Artificial Intelligence**: Complexity theory informs the feasibility of solving problems in AI, such as optimization and decision-making.

## Related Concepts
- [[Algorithm Complexity]]
- [[P vs NP Problem]]
- [[Turing Machines]]
- [[Approximation Algorithms]]

## Further Reading
- [[Computational Complexity: A Modern Approach]]
- [[The P vs NP Problem]]
- [[Randomized Algorithms and Complexity]]
