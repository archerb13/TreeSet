class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        self.size = 0
        self.root = None
        # added stuff below
        

    def __len__(self):
        return self.size

    def height(self):
        return -1

    def insert(self, item):
        if self.root:
            self.size += 1
            return self.root.insert(item)
        else:
            self.root = TreeNode(item)
            return True

    def remove(self, item):
        return False

    def __contains__(self, item):
        return False
    
    def first(self):
#        if self.root == None:
#            raise KeyError
#        elif self.root 
        raise KeyError

    def last(self):
        raise KeyError
    
    def clear(self):
        pass

    def __iter__(self):
        return iter([])
    
    

    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    # Helper functions
    # You can add additional functions here

class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)
    
    def insert(self, data):
        if self.data == data:
            return False
        
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = TreeNode(data)
                return True
            
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = TreeNode(data)
                return True
            
