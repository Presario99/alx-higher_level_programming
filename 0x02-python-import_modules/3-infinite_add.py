#!/usr/bin/python3
import sys

def add_args(args):
    result = sum(int(arg) for arg in args)
    return result

if __name__ == '__main__':
    args = sys.argv[1:]

    result = add_args(args)
    print(result)
