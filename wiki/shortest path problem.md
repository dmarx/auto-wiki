
# Shortest Path Problem

## Definition
The [[shortest path problem]] is a fundamental problem in graph theory and computer science that involves finding the shortest path between two vertices in a graph. The graph can be directed or undirected, and the edges may have weights representing distances, costs, or other metrics. The objective is to minimize the total weight of the path from a starting vertex \( s \) to a target vertex \( t \).

## Mathematical Formulation
Let \( G = (V, E) \) be a graph where:
- \( V \) is the set of vertices.
- \( E \) is the set of edges, with each edge \( (u, v) \) having a weight \( w(u, v) \).

The shortest path from vertex \( s \) to vertex \( t \) can be expressed as:

\[
\text{minimize } \sum_{(u, v) \in P} w(u, v)
\]

where \( P \) is a path from \( s \) to \( t \).

## Algorithms
Several algorithms exist to solve the shortest path problem, each suitable for different types of graphs and constraints.

### 1. Dijkstra's Algorithm
Dijkstra's algorithm is a popular method for finding the shortest path in graphs with non-negative edge weights. The algorithm maintains a priority queue of vertices, updating the shortest known distance to each vertex iteratively.

#### Steps:
1. Initialize the distance to the source vertex \( s \) as 0 and all other vertices as infinity.
2. While there are unvisited vertices:
   - Select the vertex \( u \) with the smallest distance.
   - For each neighbor \( v \) of \( u \):
     - If the distance to \( v \) through \( u \) is less than the known distance, update it.

The time complexity of Dijkstra's algorithm is \( O((V + E) \log V) \) when using a priority queue.

### 2. Bellman-Ford Algorithm
The Bellman-Ford algorithm can handle graphs with negative edge weights and detects negative weight cycles. It works by iteratively relaxing the edges.

#### Steps:
1. Initialize the distance to the source vertex \( s \) as 0 and all other vertices as infinity.
2. For \( |V| - 1 \) iterations, relax all edges:
   - For each edge \( (u, v) \):
     - If \( d[u] + w(u, v) < d[v] \), update \( d[v] \).

The time complexity of the Bellman-Ford algorithm is \( O(V \cdot E) \).

### 3. Floyd-Warshall Algorithm
The Floyd-Warshall algorithm finds the shortest paths between all pairs of vertices in a weighted graph. It uses dynamic programming to iteratively improve the path lengths.

#### Steps:
1. Initialize a distance matrix \( D \) where \( D[i][j] \) is the weight of the edge from \( i \) to \( j \) (or infinity if no edge exists).
2. For each vertex \( k \), update the distance matrix:
   \[
   D[i][j] = \min(D[i][j], D[i][k] + D[k][j])
   \]

The time complexity of the Floyd-Warshall algorithm is \( O(V^3) \).

## Applications
The shortest path problem has numerous applications, including:

- **Navigation Systems**: Finding the shortest route on maps.
- **Network Routing**: Optimizing data packet transmission in networks.
- **Urban Planning**: Analyzing transportation systems and infrastructure.

## Conclusion
The shortest path problem is a critical concept in graph theory with wide-ranging applications in computer science and engineering. Understanding the various algorithms and their complexities allows for effective problem-solving in real-world scenarios.

[[Dijkstra's algorithm]] | [[Bellman-Ford algorithm]] | [[Floyd-Warshall algorithm]] | [[graph theory]] | [[network routing]]
