
# Turing Machines

## Definition
A Turing machine is a theoretical computational model introduced by the mathematician [[Alan Turing]] in 1936. It serves as a fundamental concept in the theory of computation, providing a formal framework for understanding what it means for a function to be computable. Turing machines are used to explore the limits of what can be computed and to classify problems based on their computational complexity.

## Components of a Turing Machine
A Turing machine consists of the following components:

1. **Tape**: An infinite tape divided into discrete cells, each capable of holding a symbol from a finite alphabet \( \Sigma \). The tape serves as both input and output storage.

2. **Head**: A read/write head that can move left or right along the tape. The head can read the symbol in the current cell and write a new symbol in that cell.

3. **State Register**: A finite set of states \( Q \), including a designated start state \( q_0 \) and one or more halting states \( q_h \). The state register keeps track of the current state of the machine.

4. **Transition Function**: A function \( \delta: Q \times \Sigma \to Q \times \Sigma \times \{L, R\} \) that defines the machine's behavior. Given the current state and the symbol under the head, the transition function specifies:
   - The next state to transition to.
   - The symbol to write in the current cell.
   - The direction to move the head (left \( L \) or right \( R \)).

## Formal Definition
A Turing machine can be formally defined as a 7-tuple:
\[
M = (Q, \Sigma, \Gamma, \delta, q_0, q_h, q_a)
\]
where:
- \( Q \) is a finite set of states.
- \( \Sigma \) is the input alphabet (not including the blank symbol).
- \( \Gamma \) is the tape alphabet (including the blank symbol).
- \( \delta \) is the transition function.
- \( q_0 \) is the initial state.
- \( q_h \) is the halting state.
- \( q_a \) is the accepting state.

## Operation
The operation of a Turing machine proceeds as follows:
1. The machine starts in the initial state \( q_0 \) with the input written on the tape.
2. The head reads the symbol in the current cell.
3. The transition function \( \delta \) is applied to determine the next state, the symbol to write, and the direction to move the head.
4. The machine continues this process until it reaches a halting state \( q_h \) or an accepting state \( q_a \).

## Types of Turing Machines
1. **Deterministic Turing Machine (DTM)**: A Turing machine where the transition function \( \delta \) is deterministic, meaning that for each state and symbol, there is exactly one action to take.

2. **Non-Deterministic Turing Machine (NDTM)**: A Turing machine where the transition function can have multiple possible actions for a given state and symbol. NDTMs are used in theoretical discussions of computational complexity, particularly in the context of [[NP-completeness]].

3. **Multi-Tape Turing Machine**: An extension of the standard Turing machine that has multiple tapes and heads. This model can be shown to be equivalent in computational power to a single-tape Turing machine but can be more efficient for certain computations.

## Computational Power
Turing machines are equivalent in power to other computational models, such as [[lambda calculus]] and [[recursive functions]]. They can simulate any algorithmic process, making them a cornerstone of the Church-Turing thesis, which posits that any function that can be computed algorithmically can be computed by a Turing machine.

## Applications
Turing machines are primarily of theoretical interest but have implications in various fields:
- **Computability Theory**: They provide a framework for understanding which problems are computable and which are not.
- **Complexity Theory**: Turing machines are used to classify problems based on their computational complexity, leading to the development of complexity classes such as P, NP, and PSPACE.
- **Algorithm Design**: Insights from Turing machines inform the design and analysis of algorithms in computer science.

## Conclusion
Turing machines are a foundational concept in computer science and mathematics, providing a formal model for computation. Their study has profound implications for understanding the limits of computability and the nature of algorithms.

## Related Concepts
- [[Alan Turing]]
- [[Computability Theory]]
- [[Complexity Theory]]
- [[Church-Turing Thesis]]
- [[Lambda Calculus]]
