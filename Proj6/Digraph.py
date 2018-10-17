import math


class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        self.nodes = set()
        self.children = [{} for i in range(n)]
        # You may put any required initialization code here
        pass
    
    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        if node in self.nodes:
            return

        self.nodes.add(node)


    def insert_arc(self, s, d, w):
        """
        Inserts arc into the graph
        Raises IndexError if out of range
        Accomadates for replacements
        :param s: start number/index in self.children
        :param d: direction of s
        :param w: weight of vertice
        """
        if s not in self.nodes:
            self.add_node(s)

        if d not in self.nodes:
            self.add_node(d)
            
            
        if s not in range(0, self.order) or d not in range(0, self.order):
            raise IndexError
        if self.children[s] is None:
            self.children[s][d] = w
            self.size += 1
        else:
            if d in self.children[s]:
                self.children[s][d] = w
            else:
                self.children[s][d] = w
                self.size += 1
                

    def out_degree(self, v):
        """
        Gets the number of arrows going out of vertice
        Raise error if out of range
        :param v:  Vertice to test
        """
        if v not in range(0, self.order):
            raise IndexError
        cnt = 0
        if self.children[v] is not None:
            for item in self.children[v]:
                cnt += 1
            
        return cnt
        

    def are_connected(self, s, d):
        """
        Sees is there is an arc between s and d
        Raise error if not
        :param s: start vertice
        :param d: end vertice
        """
        if s not in range(0, self.order) or d not in range(0, self.order):
            raise IndexError
            
        if self.children[s] is None:
            return False
        
        else:
            if d in self.children[s]:
                return True
        
        return False

    def is_path_valid(self, path):
        """
        Sees if the given path is in the param
        Raise error if out of range
        :param path: path to test if in graph
        """
        size = len(path) - 1
        for index, item in enumerate(path):
            if index < size:
                if item not in range (0, self.order) or path[index +1] not in range(0, self.order):
                    raise IndexError
                    
        for index, item in enumerate(path):
            if index < size:
                if path[index +1] not in self.children[item]:
                    return False
    
        return True

    def arc_weight(self, s, d):
        """
        Finds the weight of an arc
        Raise error if vertices not in graph
        Gives math.inf if arc is missing
        :param s: starting vertice
        :param d: ending vertice
        """
        if s not in self.nodes:
            raise IndexError
            
        if d not in self.nodes:
            raise IndexError
                
        if d not in self.children[s].keys():
            return math.inf
        
        return self.children[s][d]

    def path_weight(self, path):
        """
        Gets the total weight
        Raises error if out of range when entering arc_weight
        Gives math.inf if path/arc missing
        :param path: path to test
        """
        weight = 0
        if self.is_path_valid(path):
            size = len(path) -1
            for index, item in enumerate(path):
                if index < size:
                    weight += self.arc_weight(item, path[index + 1])
        else:
            return math.inf
        
        return weight

    def does_path_exist(self, s, d):
        """
        Raises IndexError is out of range
        Creates a list to use
        Returns True if the popped item is equal to d
        Else return False
        Finds if the path exists
        :param s: starting vertice
        :param d: direction
        """
        if s not in range(0, self.order) or d not in range(0, self.order):
            raise IndexError
            
        s_list = [s]
        visited = set()
        while s_list:
            v = s_list.pop()
            if v == d:
                return True
            if v not in visited:
                visited.add(v)
                for u in self.children[v]:
                    if u not in visited:
                        s_list.append(u)
        return False

    def find_min_weight_path(self, s, d):
        pass
