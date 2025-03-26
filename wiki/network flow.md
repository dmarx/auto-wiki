
# [[Network Flow]]

## Overview
[[Network Flow]] is a mathematical framework used to model and analyze the flow of resources through a network. It is widely applicable in various fields, including operations research, computer science, and engineering. The primary objective in network flow problems is to optimize the flow of materials, information, or energy through a directed graph, subject to certain constraints.

## Definitions
A network can be represented as a directed graph \( G = (V, E) \), where:
- \( V \) is the set of vertices (or nodes),
- \( E \) is the set of directed edges (or arcs) connecting the vertices.

Each edge \( (u, v) \in E \) has an associated capacity \( c(u, v) \), which represents the maximum flow that can pass through that edge. Additionally, a flow \( f: E \rightarrow \mathbb{R} \) is defined such that:

\[
0 \leq f(u, v) \leq c(u, v) \quad \forall (u, v) \in E
\]

### Flow Conservation
For any vertex \( v \) in the network, except for the source \( s \) and sink \( t \), the flow conservation principle states that the total flow into the vertex must equal the total flow out:

\[
\sum_{u \in V} f(u, v) - \sum_{w \in V} f(v, w) = 0
\]

This condition ensures that the flow is conserved at each vertex.

## Types of Network Flow Problems
1. **Maximum Flow Problem**: The goal is to maximize the flow from a designated source \( s \) to a sink \( t \) in the network. The maximum flow \( f^* \) can be found using algorithms such as the [[Ford-Fulkerson Method]] or the [[Edmonds-Karp Algorithm]].

2. **Minimum Cut Problem**: This problem is closely related to the maximum flow problem. A cut in the network is a partition of the vertices into two disjoint subsets such that the source is in one subset and the sink is in the other. The capacity of a cut is the sum of the capacities of the edges crossing the cut. The minimum cut corresponds to the smallest capacity that separates the source from the sink, and it is equal to the maximum flow by the [[Max-Flow Min-Cut Theorem]].

3. **Circulation Problem**: In this variant, the goal is to find a flow that satisfies certain supply and demand constraints at each vertex while respecting the capacities of the edges.

## Algorithms
### Ford-Fulkerson Method
The Ford-Fulkerson method is a fundamental algorithm for computing the maximum flow in a flow network. It operates by repeatedly finding augmenting paths from the source to the sink and increasing the flow along these paths until no more augmenting paths can be found.

### Edmonds-Karp Algorithm
The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method that uses breadth-first search (BFS) to find augmenting paths. It guarantees a polynomial time complexity of \( O(VE^2) \).

### Push-Relabel Algorithm
The Push-Relabel algorithm is another approach to solving the maximum flow problem. It maintains a preflow, which allows for excess flow at vertices, and iteratively pushes flow towards the sink while maintaining the capacity constraints.

## Applications
Network flow models have a wide range of applications, including:
- **Transportation and Logistics**: Optimizing the flow of goods through supply chains.
- **Telecommunications**: Managing data flow in communication networks.
- **Project Management**: Allocating resources in project scheduling problems.
- **Traffic Engineering**: Analyzing and optimizing traffic flow in transportation networks.

## Conclusion
Network flow theory provides a robust framework for modeling and solving problems related to the flow of resources in directed graphs. The interplay between flow and capacity, along with the principles of flow conservation, forms the basis for various algorithms and applications in real-world scenarios.

## References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Ahuja, R. K., Magnanti, T. L., & Orlin, J. B. (1993). *Network Flows: Theory, Algorithms, and Applications*. Prentice Hall.
- Ford, L. R., & Fulkerson, D. R. (1956). "Maximal flow through a network." *Canadian Journal of Mathematics*, 8, 399-404.

