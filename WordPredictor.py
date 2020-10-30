class WordPredictor():

    # He said that at some point we may have to do something similar to this:
    # '[\w+]'[\w+]'
    # read file, split all lines of file into individual words, lower case all words
    # remove commas and ! and "" with regex library
    # non-alphanumeric and non apostrophes are not removed
    # re.package.whatever function, apply pattern in DictEntry or elsewhere
    # Doing it in the function is optional but it must have the capability

    def __init__(self):
        # Members: Instance variables:
        # * Map object: word_to_count -- this is a map used to store word in map. also stores total, a single variable. the total variable is separate so we can compute probability at any point
        # int total
        # * prefix_to_entry -- another map with each prefix value mapping to dictionary entry object, has the most probable word & probability of word together
        pass

    def train(self, training_file):
        pass

    def train_word(self, word):
        # start training with this, call it multiple times to test
        # each time we call this,
        # add word to Map word_to_count
        pass

    def get_training_count(self):
        # returns total (instance variable)
        pass

    def get_word_count(self, word):
        # returns count within word_to_count Map
        # word_to_count['word'] should work if Map has been implemented
        # or .get and use this as a key????
        pass

    def build(self):
        pass

    def get_best(self, prefix):
        pass


class DictEntry:
    def __init__(self, word, prob):
        pass
    # * get_word(self)
    # * get_prob(self)
    # * match_pattern(self, pattern) -- OPTIONAL

    # TODO: Hash Table and Map
    # Refer to class notes, textbooks, provided examples

    # TODO: Client and test application with keyboard_test.py


def main():
    in_file = open(r"moby_start.txt", "r")
    for line in in_file.readlines():
        print(line, end="")
    in_file.close()
    print("The file has been closed.")


main()
