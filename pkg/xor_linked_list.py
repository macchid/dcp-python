class Memory:
    def __init__(self):
        self.space = {}

    def store(self, element):
        address = hash(element)
        self.space[address] = element
        return address

    def dereference_pointer(self, pointer):
        return self.space[pointer]


mem = Memory()

class Node:
    def __init__(self, val, prev=0, next=0):
        self.val = val
        self.both = prev ^ next

    def __repr__(self):
        return f"<v:{self.val} (b:{self.both})>"

    def pointer(self):
        return hash(self)

class XORLinkedList:
    def __init__(self, root=None):
        self._root = root
        self._last = root

    def add(self, val):
        node = Node(val)
        if self._root is None:
            addr = mem.store(node)
            self._root = addr
            self._last = addr
        else:
            node.both ^= self._last
            addr = mem.store(node)
            self.last().both ^= addr
            self._last = addr

    def last(self):
        return mem.dereference_pointer(self._last)

    def root(self):
        return mem.dereference_pointer(self._root)

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        _prev = 0
        curr = self.root()
        _next = 0
        while True:
            yield curr

            _next = curr.both ^ _prev
            if _next == 0:
                break

            _prev = curr.pointer()
            curr = mem.dereference_pointer(_next)

    def get(self, index):
        steps = 0
        for n in self:
            if steps == index:
                return n
            
            steps += 1

        raise IndexError("index out of bounds exception")


if __name__ == "__main__":
    l = XORLinkedList()

    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)

    for n in l:
        print(n)

    print(l.get(0))
    print(l.get(1))
    print(l.get(3))
    print(l.get(6))