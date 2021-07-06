from collections import deque

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            self.head = LinkedNode(nodes.pop(0))
            node = self.head
            for elem in nodes:
                node.next = LinkedNode(elem)
                node = node.next

    def __repr__(self):
        nodes = [node.data for node in self]
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.add_first(node)
            return

        for current in self:
            pass

        current.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("empty list")

        for current in self:
            if current.data == target_node_data:
                new_node.next = current.next
                current.next = new_node
                return

        raise Exception(f"node with data {target_node_data} not found")

def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        return self.add_first(new_node)

    prev_node = self.head
    for node in self:
        if node.data == target_node_data:
            prev_node.next = new_node
            new_node.next = node
            return

        prev_node = node

    raise Exception(f"Node with data {target_node_data} not found")

def remove(self, target_node_data):
    if self.head is None:
        raise Exception("list is empty")

    if self.head.data == target_node_data:
        self.head = self.head.next
        return

    previous_node = self.head
    for node in self:
        if node.data == target_node_data:
            previous_node.next = node.next
            return

        previous_node = node

    raise Exception(f"node with data {target_node_data} not found")
