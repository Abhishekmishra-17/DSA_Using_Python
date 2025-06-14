# Stack Implementation Using Linked List

## Definition
A **stack** is a linear data structure that follows the Last-In-First-Out (LIFO) principle. The element inserted last is the one to be removed first. It supports two primary operations:
- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the element from the top of the stack.

## Uses of Stack
Stacks are widely used in computer science and real-world applications, including:
- **Function Call/Recursion Management**: Storing return addresses, local variables, and parameters.
- **Expression Evaluation and Syntax Parsing**: Evaluating postfix/prefix expressions, parsing expressions in compilers.
- **Undo Mechanisms**: Implementing undo features in editors.
- **Backtracking Algorithms**: Solving puzzles, navigating mazes, etc.
- **Depth-First Search (DFS)**: Traversing graphs and trees.
- **Memory Management**: Managing memory allocation in programming languages.

## Time and Space Complexity
| Operation   | Time Complexity | Space Complexity |
|-------------|----------------|-----------------|
| Push        | O(1)           | O(1)            |
| Pop         | O(1)           | O(1)            |
| Peek        | O(1)           | O(1)            |
| Size        | O(n)           | O(1)            |
| Traverse    | O(n)           | O(1)            |

## Example Usage
```python
from Stack_implementation_using_linkedlist import Stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.traverse()  # Output: 10 -> 20 -> 30 -> None
print(f"Top element: {s.peek()}")  # Output: Top element: 30
print(s.pop())  # Output: Popped: 30
s.traverse()  # Output: 10 -> 20 -> None
```

## Flow Diagram

Below is a simple flow diagram for the push and pop operations:

```
Push Operation:
[New Node] ---> [top]
   |
   v
[head] ... [top]

Pop Operation:
[top] ---> [previous node]
   |
   v
 Remove
```

## Notes
- The stack is never full (unless system memory is exhausted).
- All operations except `size` and `traverse` are O(1).
- The `pop` method now returns the popped value (or None if empty), matching the latest code update.

---

Feel free to modify or extend this implementation for your needs.
