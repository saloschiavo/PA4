class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = []
        for i in range(0, size):
            self.slots.append([])

    def put(self, item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise (no available slots, table is full)
        '''
        startslot = self.hashfunction(item)
        self.slots[startslot].append(item)
        slot = self.slots[startslot]
        indexInSlot = slot.index(item)
        return [startslot, indexInSlot]

    def get(self, item):
        '''
        returns slot position if item in hashtable, -1 otherwise
        This function resembles peek() in a stack.
        It does not modify the hash table, it just goes to see is the item there?
        Sort of like a search
        '''
        startslot = self.hashfunction(item)
        if item in self.slots[startslot]:
            slot = self.slots[startslot]
            indexInSlot = slot.index(item)
            return [startslot, indexInSlot]
        else:
            return -1

    def remove(self, item):
        '''
        Removes item
        Returns slot position if item in hashtable, -1 otherwise
        '''
        startslot = self.hashfunction(item)
        if item in self.slots[startslot]:
            # main slot
            slot = self.slots[startslot]
            # index in slot
            indexInSlot = slot.index(item)
            # This doesn't delete the item INDEX
            del self.slots[startslot][indexInSlot]
            return [startslot, indexInSlot]
        else:
            return -1

    def hashfunction(self, item):
        '''
        Remainder method
        '''
        if type(item) is int:
            return item % self.size
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size

    def __str__(self):
        '''
        Method to print
        '''
        # NOTE: KEEP THIS IN MIND, LEARN THIS
        return(str(self.slots))


# NOTE: By default, the __hash__() values of str, bytes, and datetime objects are salted with an unpredicteable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python
