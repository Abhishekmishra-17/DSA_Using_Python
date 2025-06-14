# Queue Implementation Using Linked List

This module provides a queue implementation using a singly linked list in Python.


## Definition
A **queue** is a linear data structure that follows the First-In-First-Out (FIFO) principle. The element inserted first is the one to be removed first. It supports two primary operations:
- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove an element from the front of the queue.

## Uses of Queue
Queues are widely used in computer science and real-world applications, including:
- **CPU and Disk Scheduling**: Managing processes/tasks in operating systems.
- **Breadth-First Search (BFS)**: Traversing graphs and trees.
- **Handling Requests in Web Servers**: Managing incoming requests in the order they arrive.
- **Print Queue**: Managing print jobs sent to a printer.
- **Data Buffers**: Temporary storage for data (e.g., IO Buffers, streaming data).
- **Asynchronous Data Transfer**: Communication between two processes (e.g., producer-consumer problems).


## Features
- Enqueue (add) elements to the rear
- Dequeue (remove) elements from the front
- Check if the queue is empty
- Get the front and rear elements
- Get the size of the queue
- Traverse and print the queue

## Time and Space Complexity
| Operation   | Time Complexity | Space Complexity |
|-------------|----------------|-----------------|
| Enqueue     | O(1)           | O(1)            |
| Dequeue     | O(1)           | O(1)            |
| Get Front   | O(1)           | O(1)            |
| Get Rear    | O(1)           | O(1)            |
| Get Size    | O(n)           | O(1)            |
| Traverse    | O(n)           | O(1)            |

## Example Usage
```python
from Queue_implementation_using_linkedlist import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.traverse()  # Output: 1 -> 2 -> 3 -> None
print("Front element is:", q.getFront())  # Output: 1
print("Rear element is:", q.getRear())    # Output: 3
q.dequeue()
q.traverse()  # Output: 2 -> 3 -> None
```

## Flow Diagram

Below is a simple flow diagram for the enqueue and dequeue operations:

```
Enqueue Operation:
[New Node] ---> [rear.next_add] ---> [None]
   |
   v
[front] ... [rear]

Dequeue Operation:
[front] ---> [front.next_add] ... [rear]
   |
   v
 Remove
```

## Notes
- The queue is never full (unless system memory is exhausted).
- All operations except `getsize` and `traverse` are O(1).

---

Feel free to modify or extend this implementation for your needs.
