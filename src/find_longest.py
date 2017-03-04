from collections import deque
from functools import partial
import argparse
import re
import sys

from maxheap import MaxHeap
from trie import TrieNode

SPLITTER = re.compile(r"([^\w'-])")
WORD_MATCHER = re.compile(r'\w+')


def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File containing document to analyze.')
    parser.add_argument('-k', '--top', type=int, default=5,
                        help='Number of most frequent phrases to list.')
    parser.add_argument('-l', '--min-length', dest='min_length', type=int, default=2,
                        help='Minimum length of phrases to consider.')
    parser.add_argument('-p', '--allow-punc', dest='allow_punc', action='store_true',
                        help='Allow punctuation in phrases.')
    return parser


def token_filter(token, allow_punc=False):
    if not token.strip():
        return False
    return allow_punc or WORD_MATCHER.match(token)


def sliding_window_no_whitespace(tokens, window_length, filter_func):
    window = deque(maxlen=window_length)
    for token in (t for t in tokens if filter_func(t)):
        window.append(token)
        if len(window) == window_length:
            yield tuple(window)


def main():
    args = set_up_parser().parse_args()
    tokens = [SPLITTER.split(line.lower()) for line in args.infile]
    filter_func = partial(token_filter, allow_punc=args.allow_punc)
    ngram_length = 1
    dupes = 1
    freqs = TrieNode()
    while dupes:
        dupes = 0
        for line in tokens:
            for ngram in sliding_window_no_whitespace(line, ngram_length, filter_func):
                dupes += freqs.add_phrase(ngram)
        ngram_length += 1
    heap = MaxHeap(size=args.top)
    freqs.find_top(args.top, heap, min_length=args.min_length)
    print(*heap.largest(), sep='\n')


if __name__ == '__main__':
    sys.exit(main())
