class Node:
    """
    Node class for storing data and the reference to the next node in the stack.
    """
    def __init__(self, data) -> None:
        """
        Initialize a new node with data and next address.

        Args:
            data (int): The data to store in the node.
        """
        self.data = data
        self.next_add: 'Node | None' = None  # address of next node


class Stack:
    """
    Stack implementation using a singly linked list.
    """
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.head: Node | None = None
        self.top: Node | None = None

    def traverse(self) -> None:
        """
        Print all elements in the stack from bottom to top.
        """
        tmp = self.head
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next_add
        print("None")

    def push(self, data: int) -> None:
        """
        Add an element to the top of the stack.

        Args:
            data (int): The data to push onto the stack.
        """
        new_node = Node(data)
        if self.isempty():
            self.top = new_node
            self.head = new_node
        else:
            self.top.next_add = new_node  # type: ignore
            self.top = new_node

    def pop(self) -> int | None:
        """
        Remove and return the top element of the stack.

        Returns:
            int | None: The data at the top of the stack, or None if the stack is empty.
        """
        if self.isempty():
            print("Popped: None")
            return None
        popped_data = self.top.data  # type: ignore
        if self.head == self.top:
            self.head = None
            self.top = None
        else:
            tmp = self.head
            while tmp.next_add != self.top:
                tmp = tmp.next_add
            tmp.next_add = None
            self.top = tmp
            del tmp
        print(f"Popped: {popped_data}")
        return popped_data

    def peek(self) -> int | None:
        """
        Return the top element of the stack without removing it.

        Returns:
            int | None: The data at the top of the stack, or None if the stack is empty.
        """
        if self.isempty():
            return None
        return self.top.data  # type: ignore

    def isempty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.head is None
    
    def size(self) -> int:
        """
        Get the number of elements in the stack.

        Returns:
            int: The size of the stack.
        """
        count = 0
        tmp = self.head
        while tmp:
            count += 1
            tmp = tmp.next_add
        return count

    def is_full(self) -> bool:
        """
        Check if the stack is full. Always returns False for linked list implementation.

        Returns:
            bool: False (stack is never full unless memory is exhausted).
        """
        return False


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.traverse()  # Output: 10 -> 20 -> 30 -> None
    print(f"Top element: {s.peek()}")  # Output: Top element: 30
    print(s.pop() )  # Output: Popped: 30
    s.traverse()  # Output: 10 -> 20 -> None
    print(f"Top element: {s.peek()}")  # Output: Top element: 20
    print(s.pop())  # Output: Popped: 20
    s.traverse()  # Output: 10 -> None
    print(f"Top element: {s.peek()}")  # Output: Top element: 10
    print(s.pop())  # Output: Popped: 10
    s.traverse()  # Output: None
    print(f"Top element: {s.peek()}")  # Output: Top element: None
    print(s.pop())  # Output: Popped: None
    s.traverse()  # Output: None
    print(f"Top element: {s.peek()}")  # Output: Top element: None
    s.push(40)
    s.traverse()  # Output: 40 -> None
    print(f"Top element: {s.peek()}")  # Output: Top element: 40
    print(s.pop())  # Output: Popped: 40
    s.traverse()  # Output: None
    print(f"Top element: {s.peek()}")  # Output: Top element: None
    print(s.pop())  # Output: Popped: None
    s.traverse()  # Output: None
