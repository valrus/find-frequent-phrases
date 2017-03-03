from collections import defaultdict


class KeyDefaultDict(defaultdict):
    """A defaultdict whose default method takes the key as an arg."""

    def __missing__(self, key):
        return self.default_factory(key)


class TrieNode(object):
    def __init__(self):
        self.word = None
        self.count = 0
        self.nexts = defaultdict(TrieNode)

    def add_phrase(self, phrase):
        """Add a phrase to this trie. Return whether it's been seen before.

        phrase should be an iterable of words.
        """
        curr_node = self
        for word in phrase:
            next_node = curr_node.nexts[word]
            next_node.count += 1
            curr_node = next_node
