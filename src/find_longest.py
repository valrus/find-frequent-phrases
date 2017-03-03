import argparse
import re
import sys

from trie import TrieNode

SPLITTER = re.compile(r"[^\w'-]")


def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='File containing document to analyze.')
    return parser


def main():
    args = set_up_parser().parse_args()
    for line in args.infile:
        pass


if __name__ == '__main__':
    sys.exit(main())
