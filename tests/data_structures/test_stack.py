import unittest
from pkg.data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def testPopEmpty(self):
        stack = Stack()
        with self.assertRaises(Exception) as context:
            stack.pop()
            self.assertEqual(IndexError(), context.exception)

    def testOneElement(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())

    def testMultipleConsecutiveElements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

    def testMixedOperations(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.push(3)
        stack.pop()
        stack.pop()

        stack.push(4)
        stack.push(5)
        stack.push(6)

        self.assertEqual(6, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
        
        with self.assertRaises(Exception) as context:
            stack.pop()
            self.assertEqual(IndexError(), context.exception)

if __name__ == '__main__':
    unittest.main()
            

