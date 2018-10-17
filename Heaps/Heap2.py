
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
        self.heap = []
        # Added Members

    def __len__(self):
        return 0

    def peek(self):
        raise IndexError

    def insert(self, item):
        pass

    def extract(self):
        raise IndexError

    def extend(self, seq):
        pass

    def clear(self):
        pass

    def __iter__(self):
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
    raise IndexError
