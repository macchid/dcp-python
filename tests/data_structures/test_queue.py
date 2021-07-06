import unittest
from pkg.data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def testDequeEmpty(self):
        queue = Queue()
        with self.assertRaises(Exception) as context:
            queue.dequeue()
            self.assertEqual(IndexError(), context.exception)

    def testOneElement(self):
        queue = Queue()

        queue.enqueue(1)
        self.assertEqual(1, queue.dequeue())

    def testMultipleConsecutiveElements(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

    def testMixedOperations(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.enqueue(3)
        queue.enqueue(4)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue(7)

        self.assertEqual(4, queue.dequeue())
        self.assertEqual(5, queue.dequeue())
        self.assertEqual(6, queue.dequeue())
        self.assertEqual(7, queue.dequeue())
