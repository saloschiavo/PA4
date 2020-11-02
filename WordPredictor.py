from HashTable import HashTable
from Map import Map
import re
import sys


class DictEntry:
    def __init__(self, word, prob):
        '''
        This function initializes a DictEntry object.
        '''
        self.word = word
        self.prob = prob

    def get_word(self):
        '''
        This function is used to return the word as a string
        '''
        return self.word

    def get_prob(self):
        '''
        This function is used to return the probability as a float
        '''
        return self.prob

    def match_pattern(self, pattern):
        '''
        This method matches the pattern of the words
        Returns false if an integer is entered
        Returns a boolean indicating if the words match
        '''
        if type(pattern) is int:
            return False
        return self.word == pattern.word

    def __str__(self):
        '''
        This method returns the word as a string
        '''
        return str(self.word)


class WordPredictor():
    def __init__(self):
        '''
        This function initializes the WordPredictor() class.
        Total is the total used for computing probability.
        Word_to_count is a Map used to store words.
        Prefix_to_entry is another Map that stores each prefix value that maps to a dictionary object. It contains both the most probable word and the probability of the word.
        '''
        self.total = 0
        self.word_to_count = Map()
        self.prefix_to_entry = Map()
        self.words = []

    def train(self, training_file):
        '''
        This method accepts a training_file as input and parses all lines and words.
        It prints an error if the file is not found.
        '''
        try:
            f = open(training_file, "r")
            for line in f:
                for word in line.split():
                    self.train_word(word)
            f.close()

        # returns error if file not found
        except FileNotFoundError:
            print("Could not open training file: {}".format(training_file))
            return

    def train_word(self, word):
        '''
        The train_word method utilizes a regular expression to manipulate words,
        ensuring that they are all lowercase to match, and appending them to a
        newString. Values are updated accordingly.
        '''
        # utilize RegEx
        newString = (re.sub(r'\W+', '', word)).lower()
        if self.word_to_count.get(newString) == -1:
            self.words.append(newString)
            self.word_to_count.put(newString, 1)
        else:
            value = self.word_to_count.get(newString)
            self.word_to_count.remove(newString)
            self.word_to_count[newString] = value + 1
        self.total += 1

    def get_training_count(self):
        '''
        This method returns the instance variable total
        '''
        return self.total

    def get_word_count(self, word):
        '''
        This method returns the count within the word_to_count Map.
        It returns 0 if the word is not found, and otherwise returns the word count.
        '''
        if self.word_to_count.get(word) == -1:
            return 0
        else:
            return self.word_to_count.get(word)

    def build(self):
        '''
        This method iterates through all words in word_to_count Map, building the predictions and prefixes storing in the prefix Map. It stores potential prefixes in descending order in the prefix_to_entry dictEntry. We do this multiple times for a single word.
        '''
        self.prefix_to_entry = Map()
        for word in self.words:
            count = self.word_to_count.get(word)
            prefix = ""
            for c in word:
                prefix += c
                if self.prefix_to_entry.get(prefix) == -1:
                    dictE = DictEntry(word, (count/self.total))
                    self.prefix_to_entry.put(prefix, dictE)
                else:
                    # if new probability is higher:
                    if (count/self.total) > self.prefix_to_entry.get(prefix).get_prob():
                        dictE = DictEntry(word, (count/self.total))
                        self.prefix_to_entry.remove(prefix)
                        self.prefix_to_entry.put(prefix, dictE)

    def get_best(self, prefix):
        '''
        This method gets the best match for a given prefix,
        and returns the word.
        '''
        if self.prefix_to_entry.get(prefix) == -1:
            return DictEntry("null", 0)
        else:
            return self.prefix_to_entry.get(prefix)

    def get_best_n(self, prefix):
        '''
        More advanced predictive keyboard that shows top N possible completions for current word.
        '''
        if self.prefix_to_entry.get(prefix) == -1:
            return [DictEntry("null", 0)]
        else:
            return self.prefix_to_entry.get(prefix)
