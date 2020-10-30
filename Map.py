# inherits/extends HashTable so it has all of the same methods as HashTable
# add additional list to store values

# TODO: Represent word and unigram probability as DictEntry objects
# TODO: Store word <-> word_count pairs using MAP
# TODO: Store prefix <-> DictEntry pairs using Map
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
        self.values = [None] * self.size  # holds values

    def __str__(self):
        '''
        '''
        s = ""
        for slot, key in enumerate(self.slots):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ", "
        return s

    def __len__(self):
        '''
        Return the number of key-value pairs stored in the map.
        '''
        count = 0
        for item in self.slots:
            if item is not None:
                count += 1
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
        '''
        # Find which slot item belongs to in first keys list.
        # If nothing, add linked list and add item
        # If LL exists, traverse it to see if item already exists
        # Either update item or append item to LL -- this functionality exists in parent class. We use key to call put() from HashTable to take care of adding to first list. Then we take the value and add it to the second list
        list_name = []
        # TODO: With chaining, we need slot and node location information
        slot = super().put(key)
        if slot != -1:
            # TODO: PROBABLY handle this with LL instead of Python list
            # TODO: check if list is empty, if empty, create LL and add the value in LL
            # TODO: If not empty, check the Node location and traverse through LL for Node location & add value to LL head Node. We don't need to check if it's unique because it's okay if its not
            if len(list_name) == 0:
                newList = []
                newList.append(key)
            else:
                # traverse list for Node location and add value to head
                for i in list_name:
                    if key == i:
                        # increase frequency?
                        # I know this isn't right but this is the gist of it??
                        found = True
                    if found == False:
                        list.append(key)
            self.values[slot] = value
        return -1

    def get(self, key):
        '''
        '''
        slot = super().get(key)
        if slot != -1:
            return self.values[slot]
        return -1

    def remove(self, key):
        '''
        Removes key:value pair.
        Returns slot location if item in hashtable, -1 otherwise
        '''
        slot = super().remove(key)
        if slot != -1:
            self.values[slot] = None
        return slot

    def hashfunction(self, item):
        '''
        Remainder method
        '''
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size


# Implementation example
m = Map()
m["cat"] = len("cat")
m["dog"] = len("dog")
m["lion"] = len("lion")
m["tiger"] = len("tiger")
m["bird"] = len("bird")
m["cow"] = len("cow")
m["goat"] = len("goat")
m["pig"] = len("pig")
m["chicken"] = len("chicken")

print(m)
m["llama"] = len("llama")
m["rooster"] = len("rooster")
print(m)
# hash table is full, no room to put again
m["fish"] = len("fish")
print(m)
del m["lion"]
print(m)
print(len(m))
print("cow" in m)
print("fish" in m)
