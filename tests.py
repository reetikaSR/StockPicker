import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie()

    def add_words(self):
        self.assertTrue(self.t.add_word("AICIXE"))
        self.assertTrue(self.t.add_word("AMBKP"))

    def test_words(self):
        self.t.add_word("AICIXE")
        self.t.add_word("AMBKP")
        self.assertListEqual(self.t.list_words('')[1], ["AICIXE", "AMBKP"])
        self.assertListEqual(self.t.list_words('AI')[1], ["AICIXE"])


if __name__ == '__main__':
    unittest.main()