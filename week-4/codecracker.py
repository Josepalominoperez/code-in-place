ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, n):
    index = ALPHABET.find(letter)
    new_index = (index + n) % 26
    return ALPHABET[new_index]


def encode(message, n):
    result = ""
    for char in message:
        if char in ALPHABET:
            result += shift_letter(char, n)
        else:
            result += char
    return result


def decode(message, n):
    return encode(message, -n)


def crack(message):
    for shift in range(1, 26):
        print("Shift " + str(shift) + ": " + decode(message, shift))


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    crack(message)


if __name__ == "__main__":
    main()
