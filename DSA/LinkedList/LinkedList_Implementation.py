# head, root, insert element at beg, insert element at end, insert element at index, remove first element, remove last element, remove element from a index
import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.add_next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_element_of_node(self):
        if self.head is None:
            print("Linkedlist is empty")
        while self.head:
            print(self.head.data)
            self.head = self.head.add_next_node
    
    def insert_element_at_beg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.add_next_node = self.head
            self.head = new_node

    def insert_element_at_last(self, data):
        new_node = Node(data)
        tmp = self.head
        if tmp is None:
            self.head = new_node
            tmp = None
            del(tmp)
        else:
            while tmp.add_next_node is not None:
                tmp = tmp.add_next_node
            tmp.add_next_node = new_node
            tmp = None
            del(tmp)

    def delete_element_from_beg(self):
        if self.head is None:
            print("Node is empty")
        else:
            tmp = self.head
            self.head = tmp.add_next_node
            del(tmp)

    def delete_element_from_last(self):
        pass
    
    def delete_element_from_index(self, node, index):
        a=2

root = Node(53)
linked_list = LinkedList()
linked_list.head = None
# linked_list.delete_element_from_beg()

linked_list.insert_element_at_beg(45)
linked_list.insert_element_at_last(500)
linked_list.insert_element_at_beg(425)
linked_list.insert_element_at_last(51)
linked_list.delete_element_from_beg()
# linked_list.delete_element_from_beg()

linked_list.print_element_of_node()

