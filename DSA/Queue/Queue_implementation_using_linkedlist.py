class Node:
    """
    Node class for storing data and the reference to the next node in the queue.
    """
    def __init__(self, data) -> None:
        """
        Initialize a new node with data and next address.

        Args:
            data : The data to store in the node. Can be any type.
        """
        self.data = data
        self.next_add: 'Node | None' = None  # address of next node

class Queue:
    """
    Queue implementation using a singly linked list.
    """
    def __init__(self) -> None:
        """
        Initialize an empty queue.
        """
        self.front: Node | None = None
        self.rear: Node | None = None
    
    def traverse(self) -> None:
        """
        Print all elements in the queue from front to rear.
        """
        tmp = self.front
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next_add
        else:
            print("None")
        del(tmp)

    def enqueue(self, data: int) -> None:
        """
        Add an element to the rear of the queue.

        Args:
            data (int): The data to enqueue.
        """
        new_node = Node(data)
        if self.isempty():
            self.front = new_node
        else:
            self.rear.next_add = new_node  # type: ignore
        self.rear = new_node

    def dequeue(self) -> None:
        """
        Remove an element from the front of the queue.
        """
        tmp = self.front
        if not self.isempty():
            tmp = tmp.next_add  # type: ignore
            self.front = tmp
            if self.front == None:
                self.rear = None
            del(tmp)
        else:
            print("Queue is empty")
    
    def isempty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        if self.front is None:
            return True
        else:
            return False
    
    def isfull(self) -> None:
        """
        Print a message indicating that the queue cannot be full in a linked list implementation.
        """
        print("This operation is not valid in linkedlist representation of queue because of dynamic memory allocation")

    def getFront(self) -> int:
        """
        Get the front element of the queue.

        Returns:
            int: The data at the front of the queue, or -1 if the queue is empty.
        """
        if self.isempty():
            return -1
        else:
            return self.front.data  # type: ignore

    def getRear(self) -> int:
        """
        Get the rear element of the queue.

        Returns:
            int: The data at the rear of the queue, or -1 if the queue is empty.
        """
        if self.isempty():
            return -1
        else:
            return self.rear.data  # type: ignore

    def getsize(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            int: The size of the queue.
        """
        size = 0
        tmp = self.front
        while tmp:
            size+=1
            tmp = tmp.next_add
        del(tmp)
        return size

if __name__=="__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()  # This will print "Queue is empty" since all elements are dequeued
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
    q.dequeue()  # This will also print "Queue is empty" since the queue is already empty
    q.traverse()
    print("Front element is:", q.getFront())
    print("Rear element is:", q.getRear())
    print("Size of queue is:", q.getsize())
