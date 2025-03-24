
# Bellman Equation

The [[Bellman Equation]] is a fundamental recursive relationship in dynamic programming and optimal control theory, named after Richard Bellman. It provides a way to break down complex decision-making problems into simpler subproblems, allowing for the determination of optimal policies in stochastic environments.

## Definition

In the context of a Markov Decision Process (MDP), the Bellman Equation can be expressed in terms of the value function \( V(s) \), which represents the maximum expected return achievable from state \( s \). The equation is given by:

\[
V(s) = \max_{a \in A} \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V(s') \right)
\]

where:
- \( V(s) \) is the value function at state \( s \).
- \( A \) is the set of possible actions.
- \( R(s, a) \) is the immediate reward received after taking action \( a \) in state \( s \).
- \( \gamma \) is the discount factor, \( 0 \leq \gamma < 1 \), which determines the present value of future rewards.
- \( P(s' | s, a) \) is the transition probability of moving to state \( s' \) given the current state \( s \) and action \( a \).
- \( S \) is the set of all possible states.

## Types of Bellman Equations

### Bellman Expectation Equation

For a given policy \( \pi \), the Bellman Expectation Equation describes the value function as follows:

\[
V^\pi(s) = \sum_{a \in A} \pi(a | s) \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^\pi(s') \right)
\]

where \( \pi(a | s) \) is the probability of taking action \( a \) in state \( s \) under policy \( \pi \).

### Bellman Optimality Equation

The Bellman Optimality Equation is used to find the optimal value function \( V^*(s) \):

\[
V^*(s) = \max_{a \in A} \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^*(s') \right)
\]

This equation is central to finding the optimal policy \( \pi^* \) that maximizes the expected return.

## Applications

The Bellman Equation is widely used in various fields, including:
- [[Reinforcement Learning]]: For training agents to make decisions based on rewards and penalties.
- [[Operations Research]]: In resource allocation and inventory management problems.
- [[Economics]]: For modeling dynamic systems and optimal growth.

## Numerical Solutions

Solving the Bellman Equation analytically can be challenging, especially in high-dimensional spaces. Common numerical methods include:
- **Value Iteration**: Iteratively updating the value function until convergence.
- **Policy Iteration**: Alternating between policy evaluation and policy improvement steps.

## Symbolic Notation

To model the Bellman Equation symbolically, we can define:
- \( V: S \to \mathbb{R} \) as the value function mapping states to real numbers.
- \( R: S \times A \to \mathbb{R} \) as the reward function.
- \( P: S \times A \times S \to [0, 1] \) as the transition probability function.

This formalism allows for a clear representation of the components involved in the Bellman Equation and facilitates further exploration into related topics such as [[Dynamic Programming]], [[Markov Decision Processes]], and [[Optimal Control Theory]].

## Conclusion

The Bellman Equation serves as a cornerstone in the fields of dynamic programming and optimal control, providing a structured approach to solving complex decision-making problems. Its recursive nature allows for efficient computation of optimal strategies in uncertain environments, making it a vital tool for researchers and practitioners alike.
