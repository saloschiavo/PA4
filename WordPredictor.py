class WordPredictor():

    # Members: Instance variables:
    # * word_to_count, total -- this is a map used to store word in map. also stores total, a single variable. the total variable is separate so we can compute probability at any point
    # * prefix_to_entry -- another map with each prefix value mapping to dictionary entry object, has the most probable word & probability of word together

    def __init__(self):
        pass

    def train(self, training_file):
        pass

    def train_word(self, word):
        pass

    def get_training_count(self):
        pass

    def get_word_count(self, word):
        pass

    def build(self):
        pass

    def get_best(self, prefix):
        pass

    # TODO: DictEntry class:
    # * __init__(word, prob)
    # * get_word()
    # * get_prob()
    # * match_pattern(pattern) -- OPTIONAL

    # TODO: Hash Table and Map
    # Refer to class notes, textbooks, provided examples

    # TODO: Client and test application with keyboard_test.py
