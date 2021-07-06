# This is specially useful in schedulers, 
# where the processes must be executed taking
# their priority into account.
# By default, this implements a min-heap, but it can implement
# but this could be a max-heap just passing a comparator=lambda x,y: x > y
class Heap:
    '''
        Variant of Queue that retrieves open entries in priority order (lowest first).
        Entries are typically tuples of the form:  (priority number, data).
    '''
    def __init__(self, comparator=None):
        self._heap = []
        self._comparator = comparator or (lambda x,y: x < y)

    def length(self):
        return len(self._heap)

    def peek(self):
        return self._heap[0]

    def pop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self._heap.pop()    # raises appropriate IndexError if heap is empty
        if self._heap:
            returnitem = self._heap[0]
            self._heap[0] = lastelt
            self._siftup()
            return returnitem
        return lastelt

    def push(self, item):
        self._heap.append(item)
        self._siftdown(self.length() - 1)

    def _siftdown(self, pos):
        startpos = 0
        newitem = self._heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) // 2
            if self._comparator(newitem, parent):
                self._heap[pos] = parent
                pos = parentpos
                continue
            break

        self._heap[pos] = newitem

    def _siftup(self):
        endpos = len(self._heap)
        newitem = self._heap[0]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self._comparator(self._heap[childpos], self._heap[rightpos]):
                childpos = rightpos
            # Move the smaller child up.
            self._heap[pos] = self._heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now. Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self._heap[pos] = newitem
        self._siftdown(pos)
