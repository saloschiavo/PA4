from HashTable import HashTable
from Map import Map


class WordPredictor():

    # He said that at some point we may have to do something similar to this:
    # '[\w+]'[\w+]'
    # read file, split all lines of file into individual words, lower case all words
    # remove commas and ! and "" with regex library
    # non-alphanumeric and non apostrophes are not removed
    # re.package.whatever function, apply pattern in DictEntry or elsewhere
    # Doing it in the function is optional but it must have the capability

    def __init__(self):
        # Members / Instance variables:
        # Map object: word_to_count -- this is a map used to store word in map. also stores total, a single variable. the total variable is separate so we can compute probability at any point
        self.word_to_count = Map()
        self.total = 0
        self.prefix_to_entry = Map()
        # * prefix_to_entry -- another map with each prefix value mapping to dictionary entry object, has the most probable word & probability of word together

    def train(self, training_file):
        # the train method might have to use the train_word() method
        pass

    def train_word(self, word):
        # start training with this, call it multiple times to test
        # each time we call this,
        # add word to Map word_to_count
        self.word_to_count[word] = len(word)

    def get_training_count(self):
        '''
        This method returns the instance variable total
        '''
        return self.total

    def get_word_count(self, word):
        # returns count within word_to_count Map
        # return word_to_count['word'] should work if Map has been implemented properly
        # alternatively, .get and use this as a key? idk what he meant by that
        pass

    def build(self):
        pass

    def get_best(self, prefix):
        pass


class DictEntry:
    def __init__(self, word, prob):
        self.word = word
        self.prob = prob

    def get_word(self):
        return self.word

    def get_prob(self):
        return self.prob

    def match_pattern(self, pattern):
        # TODO: This function is OPTIONAL but we have to do it one way or another
        pass

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
