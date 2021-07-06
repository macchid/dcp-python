from collections import deque

# Uses collections.deque, because this uses a 
# double-linked list which means that appends
# and deletes are done in O(1).
# Drawbacks of deque are the extra space used
# (every node stores two more references to 
# next and previous nodes) and slow random 
# access (O(n))
# The first one could be a problem for the 
# stack, but the second one isn't.
class Stack:
    def __init__(self):
        self._stack = deque()

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        return self._stack.pop()

