
class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        self.heap = [0]
        self.size = 0
        # Added Members

    def __len__(self):
        """
        Returns size of heap
        """
        return self.size

    def peek(self):
        """
        Finds the height of the tree.
        If there is no heap, raise an Error.
        """
        if len(self) == 0:
            raise IndexError
        else:
            return self.heap[1]
        
    def perc_up(self, item):
        """
        Iterates through the heap to order it correctly
        Makes the new item in correct spot then goes to next
        Prelocates to maintain property
        :param item: Item in heap to be moved to correct position
        """
        while item // 2 > 0:
            if self.comp(self.heap[item], self.heap[item // 2]):
                temp = self.heap[item//2]
                self.heap[item//2] = self.heap[item]
                self.heap[item] = temp
            item = item //2

    def insert(self, item):
        """
        Inserts into heap
        First function for insert.
        Adds size to heap.
        :param item: item in heap to be thrown into perc_up
        """
        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size)

    def extract(self):
        """
        Extracts from heap
        First function for extract.
        Returns an IndexError if the size of the heap is 0
        Subtracts the size
        Pops the item from the heap
        :param item: item in heap to be thrown into seond perc_down
        """
        if len(self) == 0:
            raise IndexError
        else:
            val = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size = self.size - 1
            self.heap.pop()
            self.prec_down(1)
            return val
        
    def prec_down(self, i):
        """
        Swaps the roots to maintain heap property
        Iterates through until item in right spot
        :param i: item in heap to be moved around
        """
        while (i*2) <= self.size:
            child = self.min_ch(i)
            if self.heap[i] > self.heap[child]:
                temp = self.heap[i]
                self.heap[i] = self.heap[child]
                self.heap[child] = temp
            i = child
            
    def min_ch(self, k):
        """
        Gets the child for the comparison in perc_down
        :param k: item in heap to compare
        """
        if k * 2 + 1 > self.size:
            return k *2
        else:
            if self.heap[k*2] < self.heap[k*2+1]:
                return k*2
            else:
                return k*2+1

    def extend(self, seq):
        """
        Inserts multiple items into the heap
        All at once instead of one at a time
        :param seq: list of items to insert into heap
        """
        for n in seq:
            self.insert(n)

    def clear(self):
        """
        Clears the heap of all items
        """
        for n in self.heap:
            self.heap.remove(n)
        self.size = 0
        self.heap = [0]

    def __iter__(self):
        """ 
        returns an iterator for the heap 
        """
        try:
            while True:
                yield self.extract()
        except IndexError:
            return
        return iter([])

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods


# Required Non-heap member function


def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq:
        raise IndexError
    min_heap = Heap(lambda a, b: a <= b)
    max_heap = Heap(lambda a, b: a >= b)
    min_heap.extend(seq)
    k = len(min_heap) // 2
    while k > 0:
        min_heap.extract()
        k = k - 1
    return min_heap.extract()
