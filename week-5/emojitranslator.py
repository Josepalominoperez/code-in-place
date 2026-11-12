def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")
    emoji_dict = build_emoji_dict()
    print("Words in your dictionary: " + str(len(emoji_dict)))
    print_emoji_dict(emoji_dict)
    while True:
        sentence = input("Enter a sentence: ")
        if sentence == "":
            break
        print(translate(sentence, emoji_dict))


def build_emoji_dict():
    emoji_dict = {}
    while True:
        word = input("Word: ")
        if word == "":
            break
        word = word.lower()
        emoji = input("Emoji for " + word + ": ")
        emoji_dict[word] = emoji
    return emoji_dict


def translate(sentence, emoji_dict):
    result = ""
    for word in sentence.split():
        lower_word = word.lower()
        if lower_word in emoji_dict:
            result += emoji_dict[lower_word] + " "
        else:
            result += word + " "
    return result


def print_emoji_dict(emoji_dict):
    for word in emoji_dict:
        print(word + ": " + emoji_dict[word])


if __name__ == "__main__":
    main()
