#!/usr/bin/python3
import sys

def add_args(args):
    # converts args to int and sum them up
    result = sum(int(arg) for arg in args)
    return result

if __name__ == '__main__':
    # Get command line args excluding script name
    args = sys.argv[1:]

    result = add_args(args)
    print(result)
