
# [[Graph Algorithms]]

## Overview
[[Graph Algorithms]] are a set of computational procedures designed to solve problems related to graph theory. These algorithms are fundamental in computer science and applied mathematics, as they provide efficient methods for processing and analyzing graphs, which are structures consisting of vertices (or nodes) connected by edges. Graph algorithms have applications in various domains, including network analysis, social network analysis, optimization problems, and more.

## Types of Graph Algorithms
Graph algorithms can be broadly categorized into several types based on their objectives and the problems they address:

### 1. Traversal Algorithms
Traversal algorithms are used to visit all the vertices of a graph systematically. The two primary traversal methods are:

- **Depth-First Search (DFS)**: This algorithm explores as far as possible along each branch before backtracking. It can be implemented using recursion or a stack. The pseudocode for DFS can be expressed as:

\[
\text{DFS}(v) \{
\begin{align*}
\text{mark } v \text{ as visited} \\
\text{for each } u \text{ adjacent to } v \text{ do} \\
\quad \text{if } u \text{ is not visited then} \\
\quad \quad \text{DFS}(u) \\
\}
\end{align*}
\]

- **Breadth-First Search (BFS)**: This algorithm explores all neighbors at the present depth prior to moving on to nodes at the next depth level. It is typically implemented using a queue. The pseudocode for BFS is:

\[
\text{BFS}(s) \{
\begin{align*}
\text{enqueue } s \text{ into queue} \\
\text{mark } s \text{ as visited} \\
\text{while queue is not empty do} \\
\quad v = \text{dequeue from queue} \\
\quad \text{for each } u \text{ adjacent to } v \text{ do} \\
\quad \quad \text{if } u \text{ is not visited then} \\
\quad \quad \quad \text{enqueue } u \text{ into queue} \\
\quad \quad \quad \text{mark } u \text{ as visited} \\
\}
\end{align*}
\]

### 2. Shortest Path Algorithms
These algorithms are designed to find the shortest path between vertices in a graph. Key algorithms include:

- **Dijkstra's Algorithm**: This algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights. The algorithm maintains a priority queue to explore the vertex with the smallest tentative distance. The pseudocode is as follows:

\[
\text{Dijkstra}(s) \{
\begin{align*}
\text{initialize } d[v] = \infty \text{ for all } v \in V \\
d[s] = 0 \\
\text{while } Q \text{ is not empty do} \\
\quad u = \text{extract-min}(Q) \\
\quad \text{for each } v \text{ adjacent to } u \text{ do} \\
\quad \quad \text{if } d[u] + w(u, v) < d[v] \text{ then} \\
\quad \quad \quad d[v] = d[u] + w(u, v) \\
\}
\end{align*}
\]

- **Bellman-Ford Algorithm**: This algorithm can handle graphs with negative weights and detects negative weight cycles. It iteratively relaxes the edges of the graph. The pseudocode is:

\[
\text{Bellman-Ford}(s) \{
\begin{align*}
\text{initialize } d[v] = \infty \text{ for all } v \in V \\
d[s] = 0 \\
\text{for } i = 1 \text{ to } |V| - 1 \text{ do} \\
\quad \text{for each edge } (u, v) \text{ do} \\
\quad \quad \text{if } d[u] + w(u, v) < d[v] \text{ then} \\
\quad \quad \quad d[v] = d[u] + w(u, v) \\
\}
\end{align*}
\]

### 3. Minimum Spanning Tree Algorithms
These algorithms find a subset of edges that connect all vertices in a graph with the minimum possible total edge weight. Notable algorithms include:

- **Kruskal's Algorithm**: This algorithm builds the minimum spanning tree by adding edges in increasing order of weight, ensuring no cycles are formed. The pseudocode is:

\[
\text{Kruskal}(G) \{
\begin