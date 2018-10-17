#################################################################
#   Project 3 TreeSet
#

#   Used some online sources for assistance, along with 

#   help from YouTube videos

#   https://www.geeksforgeeks.org // https://stackoverflow.com/

#   https://codereview.stackexchange.com

################################################################
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
        

    def __len__(self):
        """
        Returns the size of the tree.
        """
        return self.size

    def height(self):
        """
        Finds the height of the tree.
        If there is no tree, return -1.
        """
        if self.root:
            return self.root.get_height()
        else:
            return -1


    def insert(self, item):
        """
        Inserts into binary search tree
        First function for insert.
        Works with TreeSet.
        :param item: item in tree to be thrown into seond insert function
        """
        if(self.root == None):
            self.root = TreeNode(item)
            self.size += 1
            return True
        else:
            if (self.__contains__(item) == False):
                self._insert(item, self.root)
                self.size += 1
                return True
            
    def _insert(self, item, node):
        """
        Second part of insert function
        Compares the item to be inserted to other item. 
        If result is less then node, throw left.
        If result is greater, throw right
        :param item: Item comaping with
        :param node: Node that was already there to compare to item
        """
        compare = self.comp (item, node.data)
        if (compare == -1):
            if(node.left != None):
                self._insert(item, node.left)
            else:
                node.left = TreeNode(item)
        elif (compare == 1):
            if(node.right != None):
                self._insert(item, node.right)
            else:
                node.right = TreeNode(item)
        else:
            return False

    def remove(self, item):
        """ 
        Deletes key and returns new root.
        First part.
        Test to see if there is a tree, and returns False if there is not.
        Test to see if it already contains item.
        Subtracts size if removed.
        Returns True if item is removed
        :param item: Item to see if in tree and to be removed
        """
        if self.root == None:
            return False
        
        elif self.root:
            if (self.__contains__(item) == True):
                self.size -= 1
                self.root = self.root.remove(item)
                return True

    def __contains__(self, item):
        """
        Sees if item is in tree and returns true if in it
        :param item: Item to test if in tree.
        """
        return self.find_node(self.root,item)
    
    def find_node(self, current, item):
        """
        Takes item in contain and goes through each node to see if in.
        Returns True is in
        Returns False if it is not in tree
        Moves to next node depending on the compare fo current nodes.
        :param current: Node to compare with test item
        : param item: Test item
        """
        if (current is None):
            return False
        elif(item == current.data):
            return True
        elif(item < current.data):
            return self.find_node(current.left, item)
        else:
            return self.find_node(current.right, item)

    
    def first(self):
        """
        Finds first/minimal number in tree
        Returns False if tree is non-existent
        """
        if self.root == None:
            raise KeyError
        else:
            if self.root.left:
                return self.first_find(self.root.left)
            else:
                return self.root.data
                
    def first_find(self, current):
        """
        Keeps moving down the left side of tree
        Returns once cannot move anymore
        :param current: node to compared to see if bottom.
        """
        if current.left:
            return self.first_find(current.left)
        else:
            return current.data
            
        
    def last(self):
        """
        Finds last/largest number in tree
        Returns False if tree is non-existent
        """
        if self.root == None:
            raise KeyError
        else:
            if self.root.right:
                return self.last_find(self.root.right)
            else:
                return self.root.data
            
    def last_find(self, current):
        """
        Keeps moving down the right side of tree
        Returns once cannot move anymore
        :param current: node to compared to see if bottom.
        """
        if current.right:
            return self.last_find(current.right)
        else:
            return current.data
        
    
    def clear(self):
        """
        Makes size 0 and sets root to 0 to clear the whole tree
        """
        self.size = 0
        self.root = None
        
    def __iter__(self):
        """ returns an iterator for the binary search tree """
        if self.root:
            # if the tree is not empty, just return the root's iterator
            return iter(self.root)
          
    

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

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)


    def __iter__(self):
        """ 
        Return the iterator that iterates through the elements in the BST 
        rooted at this node in an inorder sequence.
        Gets iterator object on left side of tree
        Yields that ide first because we want in-order.
        Gets it for right side after
        """
        
        if self.left:
            for elt in self.left:         
                yield elt
                
        yield (self.data)
        
        if self.right:
            for elt in self.right:
                yield elt
                
    def remove(self, data):
        """
        Delete the node with the given key and return the root node of the tree
        If dat is non-existent, return self then.
        Compare to left and right and remove accordingly
        Reseting the children
        First else is for one child
        val = self._findMin is for 2 children
        Moves it into self and deltes it from val to allow usage of val again
        :param data: Data held in the nodes
        """
        if self.data is None:
            return self
            
        if data < self.data:
            self.left = self.left.remove(data)
            
        elif data > self.data:
            self.right = self.right.remove(data)
            
        else:
            if self.left is None:
                val = self.right
                self.data = None
                return val
            
            elif self.right is None:
                val = self.left
                self.data = None
                return val
            
            val = self._findMin(self.right)
            
            self.data = val.data
            
            self.right = self.right.remove(val.data)
                    
        return self
    
    def _findMin(self, node):
        """ 
        Return the minimum node in the current tree and its parent 
        Used in remove when node has two children
        :param node: node to use and send back into remove
        """

        current = node
        while(current.left is not None):
            current = current.left 
 
        return current 
    
    def get_height(self):
        """
        Gets the full height of the tree. 
        If there is a left and right side, finds max of that.
        If only left, finds height of that side
        If right, finds height of that
        If none above, returns 0
        """
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 0