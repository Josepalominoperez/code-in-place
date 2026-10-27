from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    print("Welcome to Wordle!")
    answer = get_random_word()
    for attempt in range(NUM_ATTEMPTS):
        remaining_letters = list(answer)
        guess = input("Enter your guess: ").lower()
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()
        result = []
        for i in range(5):
            if guess[i] == answer[i]:
                result.append("G")
                remaining_letters.remove(guess[i])
            else:
                result.append("B")
        for i in range(5):
            if result[i] == "B":
                if guess[i] in remaining_letters:
                    result[i] = "Y"
                    remaining_letters.remove(guess[i])
        display = []
        for i in range(5):
            if result[i] == "G":
                display.append("[" + guess[i] + "]")
            elif result[i] == "Y":
                display.append("(" + guess[i] + ")")
            else:
                display.append(guess[i])
        print("Result: " + " ".join(display))
        if guess == answer:
            print("Congratulations! You guessed the word in " + str(attempt + 1) + " tries!")
            return
    print("Better luck next time! The correct word was '" + answer + "'.")

if __name__ == "__main__":
    main()
