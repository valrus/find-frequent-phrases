from collections import deque
import argparse
import re
import sys

from .trie import TrieNode

SPLITTER = re.compile(r"([^\w'-])")


def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File containing document to analyze.')
    return parser


def sliding_window_no_whitespace(tokens, window_length):
    window = deque(maxlen=window_length)
    for token in (t for t in tokens if t.strip()):
        window.append(token)
        if len(window) == window_length:
            yield tuple(window)


def main():
    args = set_up_parser().parse_args()
    tokens = [SPLITTER.split(line) for line in args.infile]
    ngram_length, dupes = 1, 0
    done = False
    freqs = TrieNode()
    while not done:
        for line in tokens:
            for ngram in sliding_window_no_whitespace(line, ngram_length):
                freqs.add_phrase(ngram)
        done = dupes <= 1


if __name__ == '__main__':
    sys.exit(main())
