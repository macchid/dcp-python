from collections import deque

# Uses collections.deque, because this uses a 
# double-linked list which means that appends
# and deletes are done in O(1) on both sides.
# Drawbacks of deque are the extra space used
# (every node stores two more references to 
# next and previous nodes) and slow random 
# access (O(n))
# The first one could be a problem for the 
# Queue, but the second one isn't.
class Queue:
    def __init__(self):
        self._stack = deque()

    def enqueue(self, element):
        self._stack.append(element)

    def dequeue(self):
        return self._stack.popleft()
