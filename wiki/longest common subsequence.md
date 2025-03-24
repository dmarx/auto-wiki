
# Longest Common Subsequence

## Definition
The [[Longest Common Subsequence]] (LCS) problem is a classic problem in computer science and bioinformatics that seeks to find the longest subsequence common to two sequences. Unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. 

Formally, given two sequences \( X = x_1, x_2, \ldots, x_m \) and \( Y = y_1, y_2, \ldots, y_n \), the LCS is defined as the longest sequence \( Z = z_1, z_2, \ldots, z_k \) such that:

1. \( z_i \) is a member of \( X \) for some \( i \).
2. \( z_i \) is a member of \( Y \) for some \( j \).
3. The order of elements in \( Z \) is preserved in both \( X \) and \( Y \).

## Dynamic Programming Approach
The LCS can be computed efficiently using a [[dynamic programming]] approach. We define a matrix \( C \) where \( C[i][j] \) represents the length of the LCS of the first \( i \) characters of sequence \( X \) and the first \( j \) characters of sequence \( Y \).

### Initialization
The first row and column of the matrix are initialized as follows:

\[
C[i][0] = 0 \quad \text{for } i = 0, 1, \ldots, m
\]
\[
C[0][j] = 0 \quad \text{for } j = 0, 1, \ldots, n
\]

### Recurrence Relation
For \( i > 0 \) and \( j > 0 \), the recurrence relation is defined as:

\[
C[i][j] = 
\begin{cases} 
C[i-1][j-1] + 1 & \text{if } x_i = y_j \\ 
\max(C[i-1][j], C[i][j-1]) & \text{if } x_i \neq y_j 
\end{cases}
\]

This means that if the characters \( x_i \) and \( y_j \) are equal, the length of the LCS increases by 1. If they are not equal, the length of the LCS is the maximum of the lengths obtained by either excluding the current character of \( X \) or \( Y \).

### Final Result
The length of the longest common subsequence \( LCS(X, Y) \) is found in the cell \( C[m][n] \).

## Backtracking to Find the LCS
To reconstruct the actual LCS from the matrix \( C \), backtracking is performed starting from \( C[m][n] \):

1. If \( x_i = y_j \), include \( x_i \) (or \( y_j \)) in the LCS and move diagonally to \( C[i-1][j-1] \).
2. If \( x_i \neq y_j \), move in the direction of the larger value (either \( C[i-1][j] \) or \( C[i][j-1] \)).

## Complexity
The time complexity of the dynamic programming solution for LCS is \( O(m \cdot n) \), where \( m \) and \( n \) are the lengths of the sequences \( X \) and \( Y \), respectively. The space complexity is also \( O(m \cdot n) \) due to the storage of the matrix \( C \).

## Applications
The LCS problem has various applications, including:

- **Bioinformatics**: Comparing DNA, RNA, or protein sequences to identify similarities.
- **Version Control Systems**: Determining changes between file versions.
- **Natural Language Processing (NLP)**: Measuring similarity between texts.

## Conclusion
The Longest Common Subsequence problem is a fundamental problem in computer science with significant implications in various fields. Its efficient computation through dynamic programming allows for practical applications in data comparison and analysis.

[[dynamic programming]] | [[bioinformatics]] | [[natural language processing]] | [[subsequence]] | [[string matching algorithms]]
