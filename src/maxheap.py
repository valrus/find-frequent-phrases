from heapq import heappush, heappushpop, nlargest


class MaxHeap(object):
    def __init__(self, size=1):
        self.storage = []
        self.size = size

    def add(self, freq, item):
        if len(self.storage) < self.size:
            heappush(self.storage, (freq, len(item), item))
        else:
            heappushpop(self.storage, (freq, len(item), item))

    def largest(self):
        return [(' '.join(item), freq)
                for (freq, _, item) in nlargest(self.size, self.storage)]
