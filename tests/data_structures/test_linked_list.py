import unittest
from pkg.data_structures.linked_list import LinkedList, LinkedNode

class TestLinkedList(unittest.TestCase):
    

    def testAddFirst(self):
        llist = LinkedList()
        llist.add_first(LinkedNode("A"))

        self.assertEqual("A -> None", str(llist))

    def testAddLast(self):
        llist = LinkedList()
        llist.add_first(LinkedNode("A"))
        llist.add_last(LinkedNode("C"))
        llist.add_first(LinkedNode("B"))

        self.assertEqual("B -> A -> C -> None", str(llist))

    def testAddAfter(self):
        llist = LinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A -> B -> C -> D -> E -> None", str(llist))

        llist.add_after("C", LinkedNode("F"))
        self.assertEqual("A -> B -> C -> F -> D -> E -> None", str(llist))

    def testAddBefore(self):
        llist = LinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A -> B -> C -> D -> E -> None", str(llist))

        llist.add_before("C", LinkedNode("F"))
        self.assertEqual("A -> B -> F -> C -> D -> E -> None", str(llist))

    def testRemove(self):
        llist = LinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A -> B -> C -> D -> E -> None", str(llist))

        llist.remove("C")
        self.assertEqual("A -> B -> D -> E -> None", str(llist))


