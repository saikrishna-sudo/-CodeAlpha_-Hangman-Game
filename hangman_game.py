import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'programming', 'development', 'random', 'computer', 'science']

def get_random_word(word_list):
    return random.choice(word_list)

def display_current_progress(word, correct_guesses):
    display_word = ''.join([letter if letter in correct_guesses else '_' for letter in word])
    print(f"Word: {display_word}")

def play_hangman():
    word_to_guess = get_random_word(words)
    correct_guesses = set()
    incorrect_guesses = set()
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while len(incorrect_guesses) < max_incorrect_guesses:
        display_current_progress(word_to_guess, correct_guesses)
        guess = input("Guess a letter: ").lower()

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter. Try again.")
        elif guess in word_to_guess:
            correct_guesses.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess! You have {max_incorrect_guesses - len(incorrect_guesses)} incorrect guesses left.")

        if set(word_to_guess).issubset(correct_guesses):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
