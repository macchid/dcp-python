import unittest
from pkg.data_structures.double_linked_list import DoubleLinkedList, DoubleLinkedNode

class TestDoubleLinkedList(unittest.TestCase):
    

    def testAddFirst(self):
        llist = DoubleLinkedList()
        llist.add_first(DoubleLinkedNode("A"))

        self.assertEqual("A <-> None", str(llist))

    def testAddLast(self):
        llist = DoubleLinkedList()
        llist.add_first(DoubleLinkedNode("A"))
        llist.add_last(DoubleLinkedNode("C"))
        llist.add_first(DoubleLinkedNode("B"))

        self.assertEqual("B <-> A <-> C <-> None", str(llist))

    def testAddAfter(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.add_after("C", DoubleLinkedNode("F"))
        self.assertEqual("A <-> B <-> C <-> F <-> D <-> E <-> None", str(llist))

    def testAddAfterLast(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.add_after("E", DoubleLinkedNode("F"))
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> F <-> None", str(llist))

    def testAddBefore(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.add_before("C", DoubleLinkedNode("F"))
        self.assertEqual("A <-> B <-> F <-> C <-> D <-> E <-> None", str(llist))

    def testAddBeforeFirst(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.add_before("A", DoubleLinkedNode("F"))
        self.assertEqual("F <-> A <-> B <-> C <-> D <-> E <-> None", str(llist))

    def testRemove(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.remove("C")
        self.assertEqual("A <-> B <-> D <-> E <-> None", str(llist))

    def testRemoveLast(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.remove("E")
        self.assertEqual("A <-> B <-> C <-> D <-> None", str(llist))

    def testRemoveFirst(self):
        llist = DoubleLinkedList(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual("A <-> B <-> C <-> D <-> E <-> None", str(llist))

        llist.remove("A")
        self.assertEqual("B <-> C <-> D <-> E <-> None", str(llist))
