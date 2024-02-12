import sys
from ft_filter import ft_filter


def main():
    """starting"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        if ft_filter(lambda x: not x.isalnum(), sys.argv[1].split()):
            raise AssertionError("the arguments are bad")
        string = list(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                                sys.argv[1].split()))
        print(string)
    except AssertionError as msg:
        print("AssertionError:", msg)
    return


if __name__ == "__main__":
    main()
