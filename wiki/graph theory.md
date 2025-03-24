
# Graph Theory

## Definition
[[Graph Theory]] is a branch of mathematics that studies the properties and applications of graphs, which are mathematical structures used to model pairwise relations between objects. A graph \( G \) is defined as a pair \( G = (V, E) \), where \( V \) is a set of vertices (or nodes) and \( E \) is a set of edges (or links) that connect pairs of vertices.

## Basic Concepts

### Vertices and Edges
- **Vertices**: The fundamental units of a graph, often represented as points.
- **Edges**: The connections between vertices, which can be directed or undirected.
  - **Directed Graph (Digraph)**: A graph where edges have a direction, represented as ordered pairs \( (u, v) \) indicating a connection from vertex \( u \) to vertex \( v \).
  - **Undirected Graph**: A graph where edges do not have a direction, represented as unordered pairs \( \{u, v\} \).

### Degree of a Vertex
The degree of a vertex \( v \) in a graph \( G \) is the number of edges incident to \( v \). For directed graphs, we distinguish between:
- **In-degree**: The number of edges directed into \( v \).
- **Out-degree**: The number of edges directed out of \( v \).

### Subgraphs
A subgraph \( H \) of a graph \( G \) is a graph whose vertex set \( V_H \) is a subset of \( V_G \) and whose edge set \( E_H \) is a subset of \( E_G \).

### Paths and Cycles
- **Path**: A sequence of vertices \( v_1, v_2, \ldots, v_k \) such that each consecutive pair \( (v_i, v_{i+1}) \) is an edge in \( G \).
- **Cycle**: A path that starts and ends at the same vertex, with no other repetitions of vertices.

## Types of Graphs

### Simple Graph
A graph that does not contain multiple edges or loops (edges that connect a vertex to itself).

### Complete Graph
A simple graph in which every pair of distinct vertices is connected by a unique edge. The complete graph on \( n \) vertices is denoted as \( K_n \).

### Bipartite Graph
A graph whose vertices can be divided into two disjoint sets \( U \) and \( V \) such that every edge connects a vertex in \( U \) to one in \( V \). 

### Weighted Graph
A graph in which each edge has an associated weight (or cost), often used to represent distances or costs in network problems.

## Graph Representations

### Adjacency Matrix
A square matrix \( A \) used to represent a graph, where \( A[i][j] \) indicates the presence (and possibly the weight) of an edge between vertices \( i \) and \( j \). For an undirected graph, \( A[i][j] = A[j][i] \).

### Adjacency List
A collection of lists or arrays, where each list corresponds to a vertex and contains the vertices adjacent to it. This representation is often more space-efficient for sparse graphs.

## Fundamental Theorems

### Euler's Formula
For a connected planar graph \( G \) with \( V \) vertices, \( E \) edges, and \( F \) faces, Euler's formula states:
\[
V - E + F = 2
\]

### Graph Isomorphism
Two graphs \( G_1 = (V_1, E_1) \) and \( G_2 = (V_2, E_2) \) are isomorphic if there exists a bijection \( f: V_1 \to V_2 \) such that any two vertices \( u, v \in V_1 \) are adjacent in \( G_1 \) if and only if \( f(u) \) and \( f(v) \) are adjacent in \( G_2 \).

## Applications
Graph theory has applications across various fields, including:
- **Computer Science**: Data structures, algorithms, network design, and social network analysis.
- **Biology**: Modeling biological networks, such as metabolic pathways and ecological interactions.
- **Transportation**: Optimizing routes and logistics in transportation networks.

## Conclusion
Graph theory provides a powerful framework for modeling and analyzing relationships in various domains. Its rich set of concepts and theorems enables researchers to tackle complex problems in a structured manner.

[[Further Reading]]: Explore advanced topics such as [[Graph Algorithms]], [[Network Flow]], and [[Graph Coloring]] for deeper insights into the applications and complexities of graph theory.
