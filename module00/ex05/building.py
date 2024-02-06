import sys


def main():
    char_punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    try:
        if len(sys.argv) == 1:
            for line in sys.stdin:
                string = line
        elif len(sys.argv) == 2:
            string = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("if more than one argument is" +
                                 " provided to the program")
        print("The text contains", len(string), "characters:")
        print(sum(1 for char in string if char.isupper()), "upper letters")
        print(sum(1 for char in string if char.islower()), "lower letters")
        print(sum(1 for char in string if char in char_punct),
              "punctuation marks")
        print(sum(1 for char in string if char.isspace()), "spaces")
        print(sum(1 for char in string if char.isdigit()), "digits")
    except AssertionError as msg:
        print("AssertionError:", msg)
    return


if __name__ == "__main__":
    main()
