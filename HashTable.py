class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size

    def put(self, item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise (no available slots, table is full)
        '''
        # TODO: This is set up for linear probing, not chaining, we have to fix that so that it works with chaining
        # TODO: Add element. CHAINING: if LL doesn't exist, create one and add it. if LL exists, add to LL
        hashvalue = self.hashfunction(item)
        slot_placed = -1
        # empty slot or slot contains items already
        if self.slots[hashvalue] == None or self.slots[hashvalue] == item:
            self.slots[hashvalue] = item
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != item:
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue:  # we have done a full circle through hash table
                    # no available slots
                    return slot_placed

            self.slots[nextslot] = item
            slot_placed = nextslot
        return slot_placed

    def get(self, item):
        '''
        returns slot position if item in hashtable, -1 otherwise
        This function resembles peek() in a stack.
        It does not modify the hash table, it just goes to see is the item there?
        Sort of like a search
        '''
        # TODO: This should use a linked list to get to element
        startslot = self.hashfunction(item)

        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1

    def remove(self, item):
        '''
        Removes item
        Returns slot position if item in hashtable, -1 otherwise
        '''
        startslot = self.hashfunction(item)

        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
                self.slots[position] = None
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1

    def hashfunction(self, item):
        '''
        Remainder method
        '''
        return item % self.size

    def rehash(self, oldhash):
        '''
        Plus 1 rehash for linear probing, rehash with remainder method to spread out values
        '''
        # TODO: Change method definition for Chaining with a LL
        return (oldhash + 1) % self.size


# This contains list to store keys, Map contains list with values
# TODO: Keyboard word prediction: given a prefix, predict a word using unigram model
# Example: 'ab' -> 'about', 0.001473 unigram probability

# Training and Prediction: Develop training and prediction algorithm as described in PA 4

# Dictionary is implementation of ADT Map, 1-to-1 relationship between key and value
# To look up a value, we'll use a hash table with parallel array to store value at the same slot location


ht = HashTable()
print(ht.put(61))
print(ht.put(7))
print(ht.put(12))
print(ht.put(44))
print(ht.put(92))
print(ht.put(55))
print(ht.put(9))
print(ht.put(4))
print(ht.put(21))
print(ht.slots)
print(ht.put(23))
print(ht.put(39))
print(ht.slots)
# hash table is full, no room to put again
print(ht.put(90))
print(ht.slots)
print(ht.remove(55))
print(ht.slots)


# HASHING STRINGS DEMONSTRATION
c = ord("c")
a = ord("a")
t = ord("t")
print("f(\"cat\") = (%d + %d + %d) %% 11 = %d" % (c, a, t, (c + a + t) % 11))
print("f(\"tac\") = (%d + %d + %d) %% 11 = %d" % (t, a, c, (t + a + c) % 11))

# to address this issue we can instead call the special method __hash__():
cat_hash = "cat".__hash__()
tac_hash = "tac".__hash__()

print("f(\"cat\") = \"cat\".__hash__() %% 11 = %d %% 11 = %d" %
      (cat_hash, cat_hash % 11))
print("f(\"tac\") = \"tac\".__hash__() %% 11 = %d %% 11 = %d" %
      (tac_hash, tac_hash % 11))

# NOTE: By default, the __hash__() values of str, bytes, and datetime objects are salted with an unpredicteable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python
