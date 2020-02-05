#! /usr/bin/env python

"""
Super secret project name generator!

Usage:
  project_name.py: [-c] [-s SOURCE]

Options:
  -c         use a cryptographically stronger method for random numbers
  -s SOURCE  specify location of WordNet 3.x files [default: ./wn]
"""
import sys
import os
import random
import secrets

# pip install docopt (https://github.com/docopt/docopt)
from docopt import docopt 

adj_file = "index.adj"
noun_file = "index.noun"

def random_word(fname, secret=False):
    """This is optimized for single use case. If you want to generate
thousands at a time, probably a smarter strategy would be to just suck
in the whole file to a list and pick random entries from it."""
    fsize = os.stat(fname).st_size
    fh = open(fname)
    if secret:
        position = secrets.randbelow(fsize)
    else:
        position = random.randrange(fsize)
    fh.seek(position)
    fh.readline()
    rtnval = fh.readline().split()[0]
    fh.close()
    return rtnval

def file_path(path, name):
    return "%s/%s" % (path, name)

def main(args):
    wn_path = args['-s']
    adj = random_word(file_path(wn_path, adj_file))
    while '-' in adj or '_' in adj:
        adj = random_word(file_path(wn_path, adj_file))
    noun = random_word(file_path(wn_path, noun_file))
    while '-' in noun or '_' in noun or noun.endswith('ing'):
        noun = random_word(file_path(wn_path, noun_file))

    return '%s %s' % (adj.upper(), noun.upper())

if __name__ == "__main__":
    args = docopt(__doc__, version="Project Name 0.0")
    print (main(args))
