# TODO: Give unit testing a try on your own with this one; they can be really powerful for development
# TODO: For example: make one test where you put some items in and there's no colisions
# TODO: Then make one test where there's collisions on one slot
# TODO: Then make one where there's collisions on multiple slots


from Map import Map
from HashTable import HashTable
from WordPredictor import WordPredictor
import unittest


class PA4Tests(unittest.TestCase):
    def test_put(self):
        hashset = HashTable()
        hashset.put(1)
        hashset.put(9)
        hashset.put(4)
        hashset.put(6)

        # TODO: Modify this for the format of the HashSet
        self.assertEqual(str(hashset), "1, 4, 6, 9")

    def single_col(self):
        hashset = HashTable()
        hashset.put(1)
        hashset.put(9)
        hashset.put(4)
        hashset.put(6)

        # TODO: Modify this for the format of the HashSet
        self.assertEqual(str(hashset), "1, 4, 6, 9")

    def multiple_col(self):
        hashset = HashTable()
        hashset.put(1)
        hashset.put(9)
        hashset.put(4)
        hashset.put(6)

        # TODO: Modify this for the format of the HashSet
        self.assertEqual(str(hashset), "1, 4, 6, 9")


unittest.main()
