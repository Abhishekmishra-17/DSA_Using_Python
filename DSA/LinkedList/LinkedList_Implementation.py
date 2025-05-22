# head, root, insert element at beg, insert element at end, insert element at index, remove first element, remove last element, remove element from a index


class Node:
    def __init__(self, data):
        self.data = data
        self.add_next_node = None
    
    def insert_element_at_beg(self,head,data):
        new_node = Node(data)
        if head == None:
            head = new_node
        else:
            new_node.add_next_node = head
            head = new_node
        return head

    def insert_element_at_last(self,node,data):
        new_node = Node(data)
        if node is None:
            node = new_node
        while node.add_next_node is not None:
            node = node.add_next_node
        node.add_next_node = new_node
        return node


root = Node(23)
# root.add_next_node = Node(24)
# print(root.data, root.add_next_node.data, hex(id(root)), root)
a  = root.insert_element_at_beg(root,35)
b = root.insert_element_at_last(root,40)
print(a.add_next_node.add_next_node.__dict__)


    