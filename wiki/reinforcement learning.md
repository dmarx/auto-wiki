
# Reinforcement Learning

[[Reinforcement Learning]] (RL) is a subfield of machine learning concerned with how agents ought to take actions in an environment to maximize cumulative rewards. It is inspired by behavioral psychology and involves learning from the consequences of actions rather than from explicit instructions.

## Key Concepts

### Agent, Environment, and Actions

In RL, the primary components are:
- **Agent**: The learner or decision-maker that interacts with the environment.
- **Environment**: The external system with which the agent interacts, providing feedback in the form of rewards and state transitions.
- **Actions**: The set of all possible moves the agent can make in the environment, denoted as \( A \).

### States and Rewards

- **State**: A representation of the current situation of the agent in the environment, denoted as \( s \in S \), where \( S \) is the set of all possible states.
- **Reward**: A scalar feedback signal received after taking an action in a state, denoted as \( R(s, a) \), where \( a \in A \).

### Policy

A policy \( \pi \) is a mapping from states to actions, defining the agent's behavior. It can be deterministic \( \pi: S \to A \) or stochastic \( \pi(a | s) \), representing the probability of taking action \( a \) in state \( s \).

### Value Function

The value function \( V(s) \) estimates the expected return (cumulative future rewards) from state \( s \) under a policy \( \pi \):

\[
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s \right]
\]

where \( \gamma \) is the discount factor, \( 0 \leq \gamma < 1 \), which balances immediate and future rewards.

### Q-Function

The action-value function, or Q-function, \( Q^\pi(s, a) \), represents the expected return from taking action \( a \) in state \( s \) and following policy \( \pi \) thereafter:

\[
Q^\pi(s, a) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s, a_0 = a \right]
\]

## Bellman Equations in Reinforcement Learning

The Bellman equations provide a recursive relationship for the value functions:

### Bellman Expectation Equation

\[
V^\pi(s) = \sum_{a \in A} \pi(a | s) \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^\pi(s') \right)
\]

### Bellman Optimality Equation

\[
V^*(s) = \max_{a \in A} \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V^*(s') \right)
\]

## Learning Algorithms

Reinforcement learning algorithms can be broadly categorized into two types: model-free and model-based methods.

### Model-Free Methods

1. **Value-Based Methods**: These methods focus on estimating the value function or Q-function. Examples include:
   - **Q-Learning**: An off-policy algorithm that updates the Q-values based on the Bellman equation.
   - **SARSA (State-Action-Reward-State-Action)**: An on-policy algorithm that updates Q-values based on the action taken.

2. **Policy-Based Methods**: These methods directly optimize the policy without requiring a value function. Examples include:
   - **REINFORCE**: A Monte Carlo policy gradient method that updates the policy based on the returns.

### Model-Based Methods

Model-based methods involve learning a model of the environment's dynamics and using it to plan actions. This can include techniques such as:
- **Dynamic Programming**: Utilizing the Bellman equations to compute value functions.
- **Monte Carlo Tree Search (MCTS)**: A search algorithm that builds a search tree based on random sampling of actions.

## Applications

Reinforcement learning has a wide range of applications, including:
- [[Game Playing]]: Notable successes include AlphaGo and OpenAI's Dota 2 bot.
- [[Robotics]]: For training robots to perform tasks through trial and error.
- [[Autonomous Vehicles]]: For decision-making in navigation and obstacle avoidance.
- [[Healthcare]]: For personalized treatment strategies and resource allocation.

## Conclusion

Reinforcement learning is a powerful framework for solving complex decision-making problems where an agent learns to optimize its actions based on feedback from the environment. Its theoretical foundations