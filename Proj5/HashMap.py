

class HashMap:
    def __init__(self, load_factor=1.00):
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        # Other initialization code can go here
        self.len = 20
        self.size = 0
        self.count = 0
        self.map = [None]*self.len

    def __len__(self):
        """
        Returns the size of the hashmap
        """
        return self.size

    def load(self):
        """
        Makes sure the load factor does not excceed 1
        If it is 0, just return 0
        """
        if (self.count + self.size == 0): 
            return 0
        return self.count / float(self.size)
    
    def rehash (self, oldhash):
        """
        Adjusts the hashmap according to set or del
        :param oldhash: Original hash that is being adjusted
        """
        return (oldhash + 1) % self.size

    def __contains__(self, key):
        """
        Gets the indexer to use to find an item in hashmap
        Return True if key is found; otherwise, false
        :param key: Key to find in hash
        """
        hash_ = hash(key) % self.len
        g_list = self.map[hash_]
        if g_list== None:
            return False
        for i in g_list:
            if i[0] == key:
                return True
        return False

    def __getitem__(self, key):
        """
        Gets the indexer to use to find an item in hashmap
        Returns valuse at given key in hashmap
        Raise KeyError otherwise
        :param key: Key to find in hash
        """
        key_hash = hash(key) % self.len
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(key)
    

    def __setitem__(self, key, value):
        """
        Gets the indexer to use to set an item to hashmap
        Make a key, value tuple
        Return True if item is added; otherwise, false
        Rehash after to ajust to size
        :param key: Key to add to hash
        :param value: Value to add to has along with the key
        """

        key_hash = hash(key)
        key_value = (key, value)
        hash_ = key_hash % self.len
        
        if self.map[hash_] is None:
            self.map[hash_] = list([key_value])
            self.count += 1
            self.size += 1
            return True
        else:
            for ind, pair in enumerate(self.map[hash_]):
                if pair[0] == key:
                    self.map[hash_][ind] = key_value
                    return True
                else:
                    self.rehash(hash_)
            self.map[hash_].append(key_value)
            self.count += 1
            self.size += 1
            return True

    def __delitem__(self, key):
        """
        Gets the indexer to use to delete an item from the hashmap
        If nothing in hashmap, rasie KeyError
        Return True if item is deleted; otherwise, false
        Rehash after to ajust to size
        :param key: Key to delete from hash
        """
        key_hash = hash(key) % self.len
        
        if self.size == 0:
            raise KeyError(key)
        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                self.count -= 1
                self.size -= 1
                return True
            else:
                self.rehash(key_hash)
                return True  
            
        return True            

    def __iter__(self):
        """
        Iterates through the hashmap
        Yields the pairs in a visable result
        """
        for i in self.map:
            if(i):
                for v in i:
                    key = v[0]
                    value = v[1]
                    yield (key, value)

    def clear(self):
        """
        CLears the hashmap
        """
        self.len = 20
        self.size = 0
        self.count = 0
        self.map = [None]*self.len

    def keys(self):
        """
        Reutrns a set of keys from the hashmap
        """
        key_set = set()
        for i in self.map:
            if(i):
                for v in i:
                    key = v[0]
                    key_set.add(key)
        return(key_set)
                
            

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0

    # Helper functions can go here


# Required Function
def word_frequency(seq):
    """
    Iterates through the text file
    Returns a list of words used
    Throws it through the HashMap
    :param seq: Script to iterate through
    """
    end_seq = HashMap()
    for i in seq:
        if i in end_seq:
            end_seq[i] += 1
        else:
            end_seq[i] = 1
    return end_seq
