# Constants and hlper functions for creating test suites
import json

SCALAR_CX = ", but not"

def readlines(f):
    with open(f, "r") as fp:
        lines = [l.strip("\n") for l in fp.readlines()]
    return lines

def get_vocab(pos):
    return readlines(f"./wordnet_vocab/clean/vocab_{pos}.txt")

def dump_json(d, f):
    with open(f, "w") as fp:
        json.dump(d, fp, indent=2)