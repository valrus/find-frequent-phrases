from collections import defaultdict, deque
from maxheap import MaxHeap


class TrieNode(object):
    def __init__(self):
        self.count = 0
        self.nexts = defaultdict(TrieNode)

    def add_phrase(self, phrase):
        """Add a phrase to this trie. Return whether it's been seen before.

        phrase should be an iterable of words.
        """
        curr_node = self
        for word in phrase:
            next_node = curr_node.nexts[word]
            curr_node = next_node
        curr_node.count += 1
        if curr_node.count > 1:
            print('Duplicate: ', phrase)
            return True
        return False

    def find_top(self, k, heap, phrase=None):
        phrase = phrase or []
        if self.nexts:
            found_longer = self.count == 0
            for next_word, next_node in self.nexts.items():
                if next_node.count > 1:
                    next_node.find_top(k, heap, phrase + [next_word])
                found_longer |= (next_node.count >= self.count)
            if not found_longer:
                heap.add(self.count, tuple(phrase))
        else:
            heap.add(self.count, tuple(phrase))
