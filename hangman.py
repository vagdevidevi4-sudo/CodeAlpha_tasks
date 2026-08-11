import random
WORDS = ["python", "hangman", "developer", "internship", "keyboard"]
MAX_ATTEMPTS = 6
def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_player_name():
    name = ""
    while not name:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name can't be empty.\n")
    return name.capitalize()


def play_hangman(player_name):
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print(f"\n=== Welcome to Hangman, {player_name}! ===")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed. Good luck!\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print(display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_guesses}")

        guess = input(f"{player_name}, guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"🎉 Congratulations, {player_name}! You win! The word was '{word}'.")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

    print(display_progress(word, guessed_letters))
    print(f"💀 Sorry, {player_name}, you lost! The word was '{word}'.")


def main():
    player_name = get_player_name()
    play_again = "y"
    while play_again == "y":
        play_hangman(player_name)
        play_again = input(f"\n{player_name}, play again? (y/n): ").lower().strip()
    print(f"Thanks for playing, {player_name}!")


if __name__ == "__main__":
    main()
