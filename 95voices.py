#!/usr/bin/env python2
# 95voices.py, sentence splicer simulating a crowded head with lots of voices
# This work is in the Public Domain, as per:
# http://creativecommons.org/licenses/publicdomain/

import random
from sys import argv

usage = '''Usage:
./95voices.py "This is a coherent sentence." \\
  "Here comes another meaningful thought." \\
  "3 The melody of tetris, three times." \\
  "1 That makes six simultaneous thoughts!"'''

# Example output:
#   That The The This melody The melody of is makes Here tetris, three six
#   comes a of another simultaneous thoughts! meaningful tetris, three melody
#   of tetris, three times. coherent thought. sentence. times. times.


def interleave(args):
    # http://stackoverflow.com/a/10662052/3070326
    iters = sum(([iter(arg)]*len(arg) for arg in args), [])
    random.shuffle(iters)
    return map(next, iters)


def maybe_explode(parts):
    try:
        return [parts[1:]]*int(parts[0])
    except IndexError:
        # List empty (?)
        return []
    except ValueError:
        return [parts]


def splitode_all(args):
    return sum((maybe_explode(arg.split()) for arg in args), [])


def interleave_sentences(args):
    parts = interleave(list(arg.split()) for arg in args)
    return " ".join(parts)


def main(argv):
    if len(argv) < 2:
        print usage
        exit(1)
    print " ".join(interleave(splitode_all(argv[1:])))


if __name__ == '__main__':
    main(argv)
