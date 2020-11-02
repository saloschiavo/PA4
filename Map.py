from HashTable import HashTable


class Map(HashTable):
    def __init__(self, size=11):
        '''
        The map inherits its first list from HashTable class, and adds 
        second list of its own as child class
        '''
        super().__init__(size)  # holds keys
        # holds values
        self.values = []
        for i in range(0, size):
            self.values.append([])

    def __str__(self):
        '''
        This method allows us to construct a string from a Map.
        '''
        s = ""
        for slot, keys in enumerate(self.slots):
            valueslot = self.values[slot]
            for indexInSlot, key in enumerate(keys):
                value = valueslot[indexInSlot]
                s += str(key) + ":" + str(value) + ", "
        return s

    def __len__(self):
        '''
        Return the number of key-value pairs stored in the map.
        '''
        count = 0
        for item in self.slots:
            count += len(item)
        return count

    def __getitem__(self, key):
        '''
        This method gets the key.
        '''
        return self.get(key)

    def __setitem__(self, key, data):
        '''
        This method sets the key and data.
        '''
        self.put(key, data)

    def __delitem__(self, key):
        '''
        This method deletes a key.
        '''
        self.remove(key)

    def __contains__(self, key):
        '''
        This method checks to see if a key is available.
        '''
        return self.get(key) != -1

    def put(self, key, value):
        '''
        Add a new key-value pair to the map.
        '''
        location = super().put(key)
        self.values[location[0]].append(value)

    def get(self, key):
        '''
        This function obtains the key.
        It returns -1 if not found.
        '''
        location = super().get(key)
        if location != -1:
            return self.values[location[0]][location[1]]
        return -1

    def remove(self, key):
        '''
        Removes key:value pair.
        Returns slot location if item in hashtable, -1 otherwise
        '''
        location = super().remove(key)
        if location != -1:
            del self.values[location[0]][location[1]]
            return location
        return -1
