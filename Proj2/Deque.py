# Bryce Archer
class Deque:
    """
    A double-ended queue
    """

    def __init__(self):
        """
        Initializes an empty Deque
        """
        self.item = []          # Initialises the empty list
        self.left = 0           # Sets the left side = 0
        self.right = 0          # sets the right side = 0

    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque
        """
        
        return len(self.item)   # Returns the length of the list/deque

    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        """
        try:
            return self.item[0]     # Tries to see if the value is the front
        except KeyError:            # If it is not, raise an error   
            raise IndexError
            

    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """
        try:
            return self.item[-1]    # Tries to see if the value is the back
        except KeyError:            # If not raise and error
            raise IndexError

    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """
        self.item.insert(0, e)      # Puts an item in the front
        self.left -= 1              # Moves the left to be the head

    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """
        self.item.insert(-1, e)     # Puts an item in the back
        self.right += 1             # Moves right to the tail

    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """
        if self.left != self.right:     # Sees if the list is not empty
            value = self.item[0]        # If not empty, set valuse to head
            del self.item[0]            # Pop the head and return it
            return value
        else:
            raise IndexError            # Raise error if

    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """
        if self.left != self.right:     # Sees if the list is not empty
            value = self.item[-1]       # If not empty, set valuse to tail
            del self.item[-1]           # Pop the head and return it
            return value
        else:
            raise IndexError            # Raise error if

    def clear(self):
        """
        Removes all elements from the Deque
        :return:
        """
        for index, value in enumerate(self.item):   # Iterates through the list
                                                    # and indexs each
            del self.item[index]                    # deletes all of them
            

    def retain_if(self, condition):
        """
        Removes items from the Deque so that only items satisfying the given condition remain
        :param condition: A boolean function that tests elements
        """
        for index, value in enumerate(self.item):   # Itereate throught list
            if condition(value) == True:            # If the value meets the
                                                    # condition return it
                return 
            else:
                del self.item[index]                # Else delete it

    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """
        for value in self.item:                     # Iterate through list
            yield value                             # Yield the result

    # provided functions

    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

