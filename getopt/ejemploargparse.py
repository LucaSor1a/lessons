#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()

# Some reference: https://docs.python.org/2/library/argparse.html#the-add-argument-method
parser.add_argument("-f", "--file", dest = "filePath", nargs = 1, required = True, help = "Input file path")
parser.add_argument("-s", "--size", dest = "readSize", nargs = "?", default = 2048, const = 1024, type = int, help = "Reading chunks size")
# if -s | --size option is absent, use the value specified in "default" option. If it is present but with no value, use the value specified in "const" option.

args = parser.parse_args()

print(args.filePath, args.readSize)
