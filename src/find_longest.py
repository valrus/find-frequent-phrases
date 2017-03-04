from collections import deque
import argparse
import re
import sys

from maxheap import MaxHeap
from trie import TrieNode

SPLITTER = re.compile(r"([^\w'-])")


def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File containing document to analyze.')
    parser.add_argument('-k', '--top', type=int, default=5,
                        help='Number of most frequent phrases to list.')
    return parser


def sliding_window_no_whitespace(tokens, window_length):
    window = deque(maxlen=window_length)
    for token in (t for t in tokens if t.strip()):
        window.append(token)
        if len(window) == window_length:
            yield tuple(window)


def main():
    args = set_up_parser().parse_args()
    tokens = [SPLITTER.split(line.lower()) for line in args.infile]
    ngram_length = 1
    dupes = 1
    freqs = TrieNode()
    while dupes:
        dupes = 0
        for line in tokens:
            for ngram in sliding_window_no_whitespace(line, ngram_length):
                dupes += freqs.add_phrase(ngram)
        ngram_length += 1
    heap = MaxHeap(size=args.top)
    freqs.find_top(args.top, heap)
    print(*heap.largest(), sep='\n')


if __name__ == '__main__':
    sys.exit(main())
