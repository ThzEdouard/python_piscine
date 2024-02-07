import sys


def decode_string(string):
    morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'
    }
    print(" ".join(morse_dict[char] for char in string.upper()))
    return


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for char in sys.argv[1]:
            if not char.isalnum():
                if not (char == " "):
                    raise AssertionError("the arguments are bad")
        decode_string(sys.argv[1])
    except AssertionError as msg:
        print("AssertionError:", msg)
    return


if __name__ == "__main__":
    main()
