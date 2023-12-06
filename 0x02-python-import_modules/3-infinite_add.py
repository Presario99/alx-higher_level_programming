#!/usr/bin/python3
import sys


def add_args(args):
    # Convert arguments to integers and sum them up
    result = sum(int(arg) for arg in args)
    return result


if __name__ == '__main__':
    args = sys.argv[1:]
    # Get command-line arguments excluding the script name
    result = add_args(args)
    print(result)
