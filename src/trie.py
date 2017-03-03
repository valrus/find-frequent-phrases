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

    def find_top(self, k, phrase=None, heap=None):
        queue = deque([self])
        phrase = phrase or deque()
        heap = heap or MaxHeap(size=k)
        while queue:
            node = queue.popleft()
            if node.word is not None:
                phrase.append(node.word)
            if node.nexts:
                found_longer = False
                for next_node in node.nexts.values():
                    if next_node.count > 1:
                        queue.append(next_node)
                    found_longer |= (next_node.count >= node.count)
                if not found_longer:
                    heap.add(node.count, tuple(phrase))
            else:
                phrase.pop()
        return heap.largest()
