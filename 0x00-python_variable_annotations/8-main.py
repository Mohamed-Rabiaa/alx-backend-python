#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
print("{}".format(make_multiplier(2.22)(5.2)))
