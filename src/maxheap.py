from heapq import heappush, heappushpop


class MaxHeap(object):
    def __init__(self, size=1):
        self.storage = []
        self.size = size

    def add(self, freq, item):
        if len(self.storage) < self.size:
            heappush(self.storage, (-freq, item))
        else:
            heappushpop(self.storage, (-freq, item))

    def largest(self):
        return [(item, -freq) for (freq, item) in sorted(self.storage)]
