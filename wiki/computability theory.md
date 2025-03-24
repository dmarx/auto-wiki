
# Computability Theory

## Definition
Computability theory, also known as recursion theory, is a branch of mathematical logic and computer science that studies the capabilities and limitations of computational models. It focuses on what problems can be solved by algorithms and what problems are inherently unsolvable. The field provides a formal framework for understanding the nature of computation and the concept of algorithmic processes.

## Key Concepts

### Turing Machines
A Turing machine is a theoretical model of computation introduced by [[Alan Turing]] in 1936. It consists of an infinite tape divided into cells, a tape head that can read and write symbols, and a finite set of states that dictate the machine's operations. The formal definition of a Turing machine \( M \) can be expressed as a tuple:

\[
M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})
\]

where:
- \( Q \) is a finite set of states.
- \( \Sigma \) is the input alphabet (excluding the blank symbol).
- \( \Gamma \) is the tape alphabet (including the blank symbol).
- \( \delta \) is the transition function \( \delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\} \), which specifies the next state, symbol to write, and direction to move (left or right).
- \( q_0 \) is the initial state.
- \( q_{accept} \) and \( q_{reject} \) are the accepting and rejecting states, respectively.

### Recursive Functions
Recursive functions are a class of functions that can be computed by a Turing machine. They are defined using basic functions (such as zero, successor, and projection functions) and closure operations (such as composition and primitive recursion). A function \( f: \mathbb{N} \rightarrow \mathbb{N} \) is considered recursive if there exists a Turing machine that computes \( f(n) \) for any natural number \( n \).

### Decidability
A decision problem is said to be decidable if there exists an algorithm (or Turing machine) that can provide a yes or no answer for every input in a finite amount of time. Conversely, a problem is undecidable if no such algorithm exists. The classic example of an undecidable problem is the [[Halting Problem]], which asks whether a given Turing machine will halt on a specific input.

### Complexity Classes
Computability theory also intersects with computational complexity theory, which classifies problems based on the resources required to solve them. Key complexity classes include:

- **P**: The class of decision problems that can be solved by a deterministic Turing machine in polynomial time.
- **NP**: The class of decision problems for which a solution can be verified in polynomial time.
- **NP-Complete**: A subset of NP problems that are as hard as the hardest problems in NP, meaning that if any NP-complete problem can be solved in polynomial time, then all problems in NP can be solved in polynomial time.

## Applications
Computability theory has profound implications in various fields, including:

- **Computer Science**: Understanding the limits of what can be computed and the efficiency of algorithms.
- **Mathematics**: Exploring the foundations of mathematics and the nature of mathematical proofs.
- **Philosophy**: Investigating the philosophical implications of computation, including questions about the nature of mind and intelligence.

## Conclusion
Computability theory provides a rigorous framework for understanding the limits of computation and the nature of algorithmic processes. By studying Turing machines, recursive functions, and decidability, it offers insights into what can be computed and the complexity of computational problems.

## References
- [[Turing Machines]]
- [[Alan Turing]]
- [[Halting Problem]]
- [[Recursive Functions]]
- [[Complexity Classes]]
