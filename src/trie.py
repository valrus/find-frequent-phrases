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
        return curr_node.count > 1

    def find_top(self, k, heap, phrase=None):
        phrase = phrase or []
        heap = heap or MaxHeap(size=k)
        skip_this = (self.count == 0 or len(phrase) == 1)
        if self.nexts:
            for next_word, next_node in self.nexts.items():
                if next_node.count > 1:
                    next_node.find_top(k, heap, phrase + [next_word])
                skip_this |= (next_node.count >= self.count)
        if not skip_this:
            heap.add(self.count, tuple(phrase))
