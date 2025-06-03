# head, root, insert element at beg, insert element at end, insert element at index, remove first element, remove last element, remove element from a index, reverse a linkedlist, search in linkedlist
import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.add_next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_element_of_node(self):
        tmp = self.head
        if tmp is None:
            print("Linkedlist is empty")
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.add_next_node
        print("None")
    
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
        else:
            while tmp.add_next_node:
                tmp = tmp.add_next_node
            tmp.add_next_node = new_node
        tmp = None
        del(tmp)

    def insert_element_after_a_node(self, index, data):
        new_node = Node(data)
        tmp = self.head
        if tmp is None:
            print("Underflow")
        elif index < 1:
            print("overflow")
        elif index == 1 and tmp is not None:
            self.head.add_next_node = new_node
        else:
            count = 0
            for i in range(1, index):
                count+=1
                if tmp.add_next_node is None and count != index-1:
                    print("underflow")
                    break
                elif tmp.add_next_node is None and count < index:
                    print("Underflow")
                    break
                elif tmp.add_next_node is None and count == index-1:
                    tmp.add_next_node = new_node
                    break
                elif tmp.add_next_node is not None:
                    tmp = tmp.add_next_node
            if tmp.add_next_node:
                new_node.add_next_node = tmp.add_next_node
                tmp.add_next_node = new_node

    def delete_element_from_beg(self):
        tmp = self.head
        if tmp is None:
            print("Node is empty")
        else:
            self.head = tmp.add_next_node
            del(tmp)

    def delete_element_from_last(self):
        tmp = self.head
        if tmp is None:
            print("Node is empty")
        elif tmp.add_next_node is None:
            self.head = None
            del(tmp)
        else:
            while tmp.add_next_node:
                prev = tmp
                tmp = tmp.add_next_node
            prev.add_next_node = None
            del(tmp)
            del(prev)

    def delete_element_after_a_node(self, index):
        pass

    def reverse_linked_list(self):
        tmp = self.head
        if tmp is None:
            print("Linked list is empty")
        elif tmp.add_next_node is None:
            print("Linked list has only one element")
        else:
            prev = None
            current = tmp
            next  = None
            while(current is not None):
                next = current.add_next_node
                current.add_next_node = prev
                prev = current
                current = next
            self.head = prev
            del(tmp)
            del(prev)
            del(current)
            del(next)

    def search_in_linked_list(self, data):
        tmp = self.head
        if tmp is None:
            print("Linked list is empty")
            return False
        data_index_doct = dict()
        i = 1
        while tmp:
            if tmp.data == data:
                data_index_doct[i] = tmp.data
                tmp = tmp.add_next_node
                i+=1
            else:
                tmp = tmp.add_next_node
                i+=1
        del(tmp)
        if len(data_index_doct) == 0:
            print("Data not found in linked list")
            return False
        else:
            for key, item in data_index_doct.items():
                print(f"Data {item} found at index {key}")
            return data_index_doct


if __name__ == "__main__":
    root = Node(53)
    linked_list = LinkedList()
    linked_list.head = root
    linked_list.insert_element_at_beg(45)
    # linked_list.insert_element_after_a_node(1, 34)
    # linked_list.delete_element_from_beg()
    # linked_list.delete_element_from_last()
    linked_list.print_element_of_node()
    linked_list.insert_element_at_beg(45)
    linked_list.insert_element_at_last(500)
    linked_list.insert_element_at_beg(425)
    # linked_list.insert_element_at_last(51)
    # linked_list.delete_element_from_beg()
    # linked_list.delete_element_from_beg()
    # linked_list.delete_element_from_last()
    linked_list.reverse_linked_list()
    linked_list.print_element_of_node()

    linked_list.reverse_linked_list()
    linked_list.print_element_of_node()

    index_data = linked_list.search_in_linked_list(45)

    linked_list.print_element_of_node()