
# Markov Decision Processes

## Definition
A [[Markov Decision Process]] (MDP) is a mathematical framework used for modeling decision-making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are widely used in various fields, including artificial intelligence, operations research, and economics, to model sequential decision-making problems.

## Components of MDP
An MDP is defined by the following components:

1. **States (\( S \))**: A finite set of states that represent all possible situations in which the decision maker can find themselves.

2. **Actions (\( A \))**: A finite set of actions available to the decision maker. The set of actions may depend on the current state.

3. **Transition Function (\( P \))**: A function that defines the probability of transitioning from one state to another given a specific action. Formally, it is defined as:
   \[
   P(s' | s, a) = \Pr(S_{t+1} = s' | S_t = s, A_t = a)
   \]
   where \( s \) is the current state, \( a \) is the action taken, and \( s' \) is the next state.

4. **Reward Function (\( R \))**: A function that assigns a numerical reward to each state-action pair, indicating the immediate benefit of taking action \( a \) in state \( s \):
   \[
   R(s, a) = \mathbb{E}[R_t | S_t = s, A_t = a]
   \]

5. **Discount Factor (\( \gamma \))**: A factor \( \gamma \in [0, 1] \) that determines the present value of future rewards. It is used to discount future rewards, reflecting the idea that immediate rewards are generally more valuable than future rewards.

## Objective
The objective in an MDP is to find a policy \( \pi \) that maximizes the expected cumulative reward over time. A policy is a mapping from states to actions:
\[
\pi: S \rightarrow A
\]

The value function \( V^\pi(s) \) for a policy \( \pi \) is defined as the expected return (cumulative reward) starting from state \( s \) and following policy \( \pi \):
\[
V^\pi(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t R(S_t, A_t) | S_0 = s, A_t = \pi(S_t)\right]
\]

## Bellman Equations
The Bellman equation provides a recursive decomposition of the value function. For a given policy \( \pi \), the Bellman equation is expressed as:
\[
V^\pi(s) = R(s, \pi(s)) + \gamma \sum_{s' \in S} P(s' | s, \pi(s)) V^\pi(s')
\]

The optimal value function \( V^*(s) \) satisfies the following Bellman optimality equation:
\[
V^*(s) = \max_{a \in A} \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^*(s') \right)
\]

## Solution Methods
Several methods exist for solving MDPs, including:

1. **Value Iteration**: An iterative algorithm that updates the value function until convergence. It uses the Bellman optimality equation to improve the value estimates.

2. **Policy Iteration**: An iterative method that alternates between policy evaluation (calculating the value function for a fixed policy) and policy improvement (updating the policy based on the value function).

3. **Q-Learning**: A model-free reinforcement learning algorithm that learns the value of action-state pairs directly, allowing for the estimation of the optimal policy without a model of the environment.

## Applications
MDPs are widely used in various applications, including:

- **Robotics**: For path planning and decision-making under uncertainty.
- **Finance**: In portfolio management and investment strategies.
- **Game Theory**: For modeling strategic interactions in competitive environments.
- **Healthcare**: In treatment planning and resource allocation.

## Conclusion
Markov Decision Processes provide a robust framework for modeling and solving decision-making problems under uncertainty. Understanding the components, objectives, and solution methods of MDPs is essential for applying them effectively in various domains.

[[reinforcement learning]] | [[value iteration]] | [[policy iteration]] | [[Q-learning]] | [[Bellman equation]]
