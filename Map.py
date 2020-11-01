# inherits/extends HashTable so it has all of the same methods as HashTable
# add additional list to store values

# TODO: Represent word and unigram probability as DictEntry objects
# TODO: Store word <-> word_count pairs using MAP
# TODO: Store prefix <-> DictEntry pairs using MAP
# compare probability before doing update
# prefix_to_entry['w'] = {'whale', 0.1}

from HashTable import HashTable


class Map(HashTable):
    def __init__(self, size=11):
        '''
        Method description
        NOTE: Each of these is a list, so the Map class includes 2 lists: one for keys, one for values
        Inherits first list from HashTable class
        Adds second list of its own as child class
        '''
        super().__init__(size)  # holds keys
        # holds values
        self.values = []
        for i in range(0, size):
            self.values.append([])

    def __str__(self):
        '''
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
        '''
        return self.get(key)

    def __setitem__(self, key, data):
        '''
        '''
        self.put(key, data)

    def __delitem__(self, key):
        '''
        '''
        self.remove(key)

    def __contains__(self, key):
        '''
        '''
        return self.get(key) != -1

    def put(self, key, value):
        '''
        Add a new key-value pair to the map. If the key is already in the map, then replace the old value with the new value.
        Returns the item if it is stored, or returns -1 if the item is not in the list.
        '''
        location = super().put(key)
        self.values[location[0]].append(value)

    def get(self, key):
        '''
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
