class DoubleLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data

    def add_after(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self

        self.next = node

    def add_before(self, node):
        if self.prev is not None:
            self.prev.add_after(node)
        elif node is not None:
            node.next = self

        self.prev = node

    def remove(self, node):
        if node.next is not None:
            node.next.prev = self
        
        self.next = node.next

    def make_head(self):
        self.prev = None

class DoubleLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None

        if nodes is not None:
            self.head = DoubleLinkedNode(nodes.pop(0))
            self.tail = self.head
            
            node = self.head
            for elem in nodes:
                node.add_after(DoubleLinkedNode(elem))
                node = node.next
            self.tail = node

    def __repr__(self):
        nodes = [node.data for node in self.forward()]
        nodes.append("None")
        return " <-> ".join(nodes)

    def forward(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def backwards(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.prev

    def add_first(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
            return 

        self.head.add_before(new_node)
        self.head = new_node

    def add_last(self, new_node):
        if self.tail is None:
            self.head = self.tail = new_node
            return

        self.tail.add_after(new_node)
        self.tail = new_node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("empty list")

        for current in self.forward():
            if current.data == target_node_data:
                current.add_after(new_node)
#                new_node.add_after(current.next)
                if self.tail == current:
                    self.tail = new_node

                return

        raise Exception(f"node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for current in self.backwards():
            if current.data == target_node_data:
#                new_node.add_before(current.prev)
                current.add_before(new_node)
                if self.head == current:
                    self.head = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("list is empty")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous = self.head
        for node in self.forward():
            if node.data == target_node_data:
                previous.remove(node)
                return

            previous = node


        raise Exception(f"node with data {target_node_data} not found")
