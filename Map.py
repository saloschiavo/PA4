# inherits/extends HashTable so it has all of the same methods as HashTable
# add additional list to store values

# TODO: Represent word and unigram probability as DictEntry objects
# TODO: Store word <-> word_count pairs using MAP
# TODO: Store prefix <-> DictEntry pairs using Map

class Map(HashTable):
    def __init__(self, size=11):
        super().__init__(size)
        self.values = [None] * self.size  # holds values

    def __str__(self):
        # TODO: Add method definition
        pass

    def __len__(self):
        # TODO: Add method definition
        pass

    def __getitem__(self, key):
        # TODO: Add method definition
        pass

    def __setitem__(self, key, data):
        # TODO: Add method definition
        pass

    def __delitem__(self, key):
        # TODO: Add method definition
        pass

    def __contains__(self, key):
        # TODO: Add method definition
        pass

    def put(self, key, value):
        # TODO: Add method definition
        pass

    def get(self, key):
        # TODO: Add method definition
        pass

    def remove(self, key):
        # TODO: Add method definition
        pass

    def hashfunction(self, item):
        # TODO: Add method definition
        pass
