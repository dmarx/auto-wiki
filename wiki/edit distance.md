
# Edit Distance

## Definition
The [[edit distance]] (also known as Levenshtein distance) is a metric used to quantify how dissimilar two strings (or sequences) are by counting the minimum number of operations required to transform one string into the other. The allowable operations typically include:

1. **Insertion**: Adding a character to the string.
2. **Deletion**: Removing a character from the string.
3. **Substitution**: Replacing one character with another.

Mathematically, if we denote two strings as \( A \) and \( B \), the edit distance \( d(A, B) \) can be formally defined as:

\[
d(A, B) = \min \{ \text{cost}(A, B) \}
\]

where \( \text{cost}(A, B) \) is the total cost of the operations needed to convert \( A \) into \( B \).

## Dynamic Programming Approach
The edit distance can be efficiently computed using a [[dynamic programming]] approach. We define a matrix \( D \) where \( D[i][j] \) represents the edit distance between the first \( i \) characters of string \( A \) and the first \( j \) characters of string \( B \).

### Initialization
The first row and column of the matrix are initialized as follows:

\[
D[i][0] = i \quad \text{for } i = 0, 1, \ldots, m
\]
\[
D[0][j] = j \quad \text{for } j = 0, 1, \ldots, n
\]

where \( m \) and \( n \) are the lengths of strings \( A \) and \( B \), respectively.

### Recurrence Relation
For \( i > 0 \) and \( j > 0 \), the recurrence relation is defined as:

\[
D[i][j] = \min \begin{cases} 
D[i-1][j] + 1 \\ 
D[i][j-1] + 1 \\ 
D[i-1][j-1] + \text{cost}(A[i], B[j]) 
\end{cases}
\]

where \( \text{cost}(A[i], B[j]) \) is defined as:

\[
\text{cost}(A[i], B[j]) = 
\begin{cases} 
0 & \text{if } A[i] = B[j] \\ 
1 & \text{if } A[i] \neq B[j] 
\end{cases}
\]

### Final Result
The edit distance \( d(A, B) \) is found in the cell \( D[m][n] \).

## Applications
Edit distance has numerous applications in various fields, including:

- **Natural Language Processing (NLP)**: Spell checking, autocorrect, and text similarity.
- **Bioinformatics**: Comparing DNA, RNA, or protein sequences.
- **Data Deduplication**: Identifying similar records in databases.

## Variants
Several variants of edit distance exist, including:

- **Weighted Edit Distance**: Different costs can be assigned to different operations.
- **Damerau-Levenshtein Distance**: Allows for transpositions of adjacent characters as a single operation.
- **Hamming Distance**: A special case of edit distance where only substitutions are allowed, applicable only to strings of equal length.

## Conclusion
The edit distance is a fundamental concept in string processing and comparison, providing a quantitative measure of similarity that can be leveraged in various computational applications. Its efficient computation through dynamic programming makes it a practical tool in both theoretical and applied contexts.

[[dynamic programming]] | [[Levenshtein distance]] | [[Hamming distance]] | [[Natural Language Processing]] | [[Bioinformatics]]
