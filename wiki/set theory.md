
# Set Theory

## Definition
[[Set Theory]] is a branch of mathematical logic that studies sets, which are collections of objects. These objects can be anything: numbers, symbols, points in space, or even other sets. Set theory provides a foundational framework for mathematics, allowing for the formalization of concepts such as functions, relations, and cardinality.

## Basic Concepts

### Sets
A set is typically denoted by curly braces. For example, the set of natural numbers less than 5 can be expressed as:
\[
A = \{0, 1, 2, 3, 4\}
\]

### Elements
The objects contained in a set are called elements or members. If \( x \) is an element of a set \( A \), we write:
\[
x \in A
\]
If \( x \) is not an element of \( A \), we write:
\[
x \notin A
\]

### Types of Sets
- **Empty Set**: The set containing no elements, denoted as \( \emptyset \) or \( \{\} \).
- **Finite Set**: A set with a finite number of elements, e.g., \( \{1, 2, 3\} \).
- **Infinite Set**: A set with an infinite number of elements, e.g., the set of natural numbers \( \mathbb{N} = \{0, 1, 2, \ldots\} \).
- **Subset**: A set \( A \) is a subset of a set \( B \) if every element of \( A \) is also an element of \( B \), denoted as \( A \subseteq B \).

### Operations on Sets
- **Union**: The union of two sets \( A \) and \( B \) is the set of elements that are in either \( A \) or \( B \) (or both), denoted as:
\[
A \cup B = \{ x \mid x \in A \text{ or } x \in B \}
\]

- **Intersection**: The intersection of two sets \( A \) and \( B \) is the set of elements that are in both \( A \) and \( B \), denoted as:
\[
A \cap B = \{ x \mid x \in A \text{ and } x \in B \}
\]

- **Difference**: The difference of two sets \( A \) and \( B \) (also called the complement of \( B \) in \( A \)) is the set of elements that are in \( A \) but not in \( B \), denoted as:
\[
A - B = \{ x \mid x \in A \text{ and } x \notin B \}
\]

- **Complement**: The complement of a set \( A \) refers to the elements not in \( A \) relative to a universal set \( U \), denoted as:
\[
A' = U - A
\]

## Cardinality
The cardinality of a set \( A \), denoted as \( |A| \), is a measure of the "number of elements" in the set. For finite sets, this is simply the count of elements. For infinite sets, cardinality can be more complex:
- **Countably Infinite**: A set is countably infinite if its elements can be put into a one-to-one correspondence with the natural numbers, e.g., \( \mathbb{N} \).
- **Uncountably Infinite**: A set is uncountably infinite if it cannot be put into a one-to-one correspondence with the natural numbers, e.g., the set of real numbers \( \mathbb{R} \).

## Axiomatic Set Theory
Set theory can be formalized through axioms, the most notable being the [[Zermelo-Fraenkel Set Theory]] (ZF), often combined with the Axiom of Choice (ZFC). Key axioms include:
- **Axiom of Extensionality**: Two sets are equal if they have the same elements.
- **Axiom of Pairing**: For any two sets, there exists a set that contains exactly those two sets.
- **Axiom of Union**: For any set, there exists a set that contains all the elements of the subsets of that set.

## Applications
Set theory serves as a foundational framework for various branches of mathematics, including:
- **Logic**: Formalizing logical statements and proofs.
- **Topology**: Studying properties of space that are preserved under continuous transformations.
- **Measure Theory**: Formulating concepts of size and integration.

## Conclusion
Set theory is a fundamental area of mathematics that provides the language and structure for discussing collections of objects. Its principles underpin much of modern mathematics and logic, making it essential for advanced study in