import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
    except AssertionError as msg:
        print("AssertionError:", msg)
    return


if __name__ == "__main__":
    main()
