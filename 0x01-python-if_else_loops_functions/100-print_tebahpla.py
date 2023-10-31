#!/usr/bin/python3
for idx in range(26):
    unicode = 122 - idx if idx % 2 == 0 else 122 - idx - 32
    print("{}".format(chr(unicode)), end="")
