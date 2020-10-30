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
        # TODO: Figure out if this works??
        if type(pattern) is int:
            return False
        return self.word == pattern.word

        # TODO: Hash Table and Map
        # Refer to class notes, textbooks, provided examples
        # TODO: Client and test application with keyboard_test.py


class WordPredictor():
    # He said that at some point we may have to do something similar to this:
    # '[\w+]'[\w+]'
    # read file, split all lines of file into individual words, lower case all words
    # remove commas and ! and "" with regex library
    # non-alphanumeric and non apostrophes are not removed
    # re.package.whatever function, apply pattern in DictEntry or elsewhere
    # Doing it in the function is optional but it must have the capability

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

    def train(self, training_file):
        try:
            f = open(training_file, "r")
            # for line in
            for line in training_file:
                for word in line.split():
                    self.train_word(word)
            f.close()

        except FileNotFoundError:
            print("Could not open training file: {}".format(training_file))
            return

    def train_word(self, word):
        # utilize RegEx
        newString = (re.sub(r'\W+', '', word)).lower()
        if self.word_to_count.get(newString) == -1:
            self.word_to_count.put(newString, 1)
        else:
            value = self.word_to_count.get(newString)
            self.word_to_count.put(newString, value + 1)
        # start training with this, call it multiple times to test
        # each time we call this, add word to Map word_to_count
        self.word_to_count[word] = len(word)
        self.total += 1

    def get_training_count(self):
        '''
        This method returns the instance variable total
        '''
        return self.total

    def get_word_count(self, word):
        # returns count within word_to_count Map
        # return word_to_count['word'] should work if Map has been implemented properly
        # alternatively, .get and use this as a key? idk what he meant by that
        if self.word_to_count.get(word) == -1:
            return 0
        else:
            return self.word_to_count.get(word)

    def build(self):
        '''
        This method iterates through all words, building the predictions and prefixes storing in the prefix Map. It stores potential prefixes in descending order.
        '''
        for t in (self.word_to_count.slots):
            if t is None:
                continue
            for key in t:
                if key is None:
                    continue
                prefix = ""
                dictE = DictEntry(key.key, key.value / self.total)
                for c in key.key:
                    prefix += c
                    if self.prefix_to_entry.get(prefix) == -1:
                        self.prefix_to_entry.put(prefix, [dictE])
                    else:
                        item = self.prefix_to_entry.get(prefix)
                        if item[0].get_prob() < dictE.get_prob():
                            item.insert(0, dictE)
                        elif item.count(dictE) > 0 and item[item.index()].get_prob() < dictE.get_prob():
                            item[item.index()] = dictE
                        else:
                            item.append(dictE)
                        self.prefix_to_entry.put(prefix, item)

    def get_best(self, prefix):
        '''
        This method gets the best match for a given prefix,
        and returns the word as a string.
        '''
        if self.prefix_to_entry.get(prefix) == -1:
            return DictEntry("null", 0)
            # if we're looking to get all best matches
            # return [DictEntry("null", 0)]
        else:
            return self.prefix_to_entry.get(prefix)

    def get_best_n(self, prefix):
        '''
        More advanced predictive keyboard that shows top N possible completions for current word. Letters should be labeled with numbers 0 up to N-1??
        '''
        # TODO: Bonus function?? Not sure if this works
        if self.prefix_to_entry.get(prefix) == -1:
            return [DictEntry("null", 0)]
        else:
            return self.prefix_to_entry.get(prefix)


def main():
    print("Hello World.")

    test = WordPredictor()
    inp = input("Type mobydick.txt with .txt\n")
    print("Training on: {}".format(inp))
    test.train(inp)
    print("Total words: {}".format(test.get_training_count()))
    test.build()
    inp = ""
    print("Please type in prefix to get best match or type \"exit\" to exit program")
    while inp != "exit":
        inp = input("Prefix: ")
        if inp == "exit":
            break
        print("Best matches are: ")
        index = 0
        for t in test.get_best(inp.lower()):
            print("{}: {}\n".format(index + 1, t.get_word()))
            index += 1
            if index == int(sys.argv[1]):
                break


if __name__ == "__main__":
    main()
