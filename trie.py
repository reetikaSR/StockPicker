class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for char in word:
            c = ord(char) - ord('A')
            if curr.children[c] is None:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isLast = True
        return True

    def list_words(self, prefix):
        curr = self.root
        for char in prefix:
            c = ord(char) - ord('A')
            curr = curr.children[c]
            if curr is None:
                return False, None
        if curr.isLast:
            return True, None
        prefixed_words = list()
        self.__get_prefixed_words(curr, prefixed_words, prefix)
        return False, prefixed_words

    def __get_prefixed_words(self, node, words_list, generated_word):
        if node.isLast:
            words_list.append(generated_word)
        for i in range(26):
            if node.children[i] is not None:
                self.__get_prefixed_words(node.children[i], words_list, generated_word + chr(ord('A') + i))
