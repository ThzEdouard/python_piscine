import sys

if len(sys.argv) == 1:
    exit()

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif not sys.argv[1].isdigit():
        raise AssertionError("argument is not an integer")
    if not int(sys.argv[1]) % 2:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print("AssertionError:", msg)
