
# Network Theory

## Definition
[[Network theory]] is a field of study that focuses on the structure, dynamics, and behavior of networks, which are mathematical representations of a set of objects (nodes) connected by links (edges). This theory is applicable across various disciplines, including computer science, sociology, biology, and engineering, providing insights into the relationships and interactions within complex systems.

## Mathematical Formalism
A network can be formally represented as a graph \( G = (V, E) \), where:
- \( V \) is a set of vertices (or nodes),
- \( E \) is a set of edges (or links) that connect pairs of vertices.

### Types of Networks
1. **Directed Networks**: In directed networks, edges have a direction, indicating a one-way relationship. The graph is represented as \( G = (V, E) \) where \( E \subseteq V \times V \).
2. **Undirected Networks**: In undirected networks, edges do not have a direction, indicating a mutual relationship. The edges are represented as \( E \subseteq \{(u, v) | u, v \in V\} \) with \( u \sim v \) denoting an edge between nodes \( u \) and \( v \).
3. **Weighted Networks**: In weighted networks, edges have associated weights that represent the strength or capacity of the connection. The weight of an edge \( e_{uv} \) connecting nodes \( u \) and \( v \) can be denoted as \( w_{uv} \).

### Adjacency Matrix
The structure of a network can be represented using an adjacency matrix \( A \), where the element \( A_{ij} \) indicates the presence (and possibly the weight) of an edge between nodes \( i \) and \( j \):

\[
A_{ij} = 
\begin{cases} 
1 & \text{if there is an edge from } i \text{ to } j \\
0 & \text{otherwise}
\end{cases}
\]

For weighted networks, \( A_{ij} \) would represent the weight of the edge.

## Key Concepts
### Degree of a Node
The degree \( d_i \) of a node \( i \) in an undirected network is defined as the number of edges connected to it:

\[
d_i = \sum_{j} A_{ij}
\]

In directed networks, we distinguish between in-degree \( d_{i}^{in} \) and out-degree \( d_{i}^{out} \):

\[
d_{i}^{in} = \sum_{j} A_{ji}, \quad d_{i}^{out} = \sum_{j} A_{ij}
\]

### Path and Connectivity
A path in a network is a sequence of edges that connects a sequence of nodes. The connectivity of a network can be analyzed through concepts such as:
- **Connected Components**: Subsets of nodes such that there is a path between any two nodes within the subset.
- **Shortest Path**: The minimum-length path between two nodes, often calculated using algorithms such as Dijkstra's or the Floyd-Warshall algorithm.

### Centrality Measures
Centrality measures quantify the importance of a node within a network. Common measures include:
- **Degree Centrality**: The number of direct connections a node has.
- **Betweenness Centrality**: The extent to which a node lies on the shortest paths between other nodes, calculated as:

\[
C_B(i) = \sum_{j \neq i \neq k} \frac{\sigma_{jk}(i)}{\sigma_{jk}}
\]

where \( \sigma_{jk} \) is the total number of shortest paths from node \( j \) to node \( k \), and \( \sigma_{jk}(i) \) is the number of those paths that pass through node \( i \).

## Applications
Network theory has a wide range of applications, including:
- **Social Networks**: Analyzing relationships and interactions among individuals or groups.
- **Biological Networks**: Studying interactions within biological systems, such as protein-protein interaction networks.
- **Transportation Networks**: Optimizing routes and flows in logistics and transportation systems.
- **Computer Networks**: Understanding the structure and performance of communication networks.

## Conclusion
Network theory provides a robust framework for analyzing complex systems characterized by interconnected components. Its mathematical foundations and diverse applications make it an essential area of study in both theoretical and applied contexts.

## References
- Newman, M. E. J. (2010). *Networks: An Introduction*. Oxford University Press.
- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press.

[[Graph Theory]] | [[Complex Networks]] | [[Social Network Analysis]]
