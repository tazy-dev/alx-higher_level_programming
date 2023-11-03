#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)

    if argc == 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
    for idx in range(1, argc):
        print("{}: {}".format(idx, sys.argv[idx]))
