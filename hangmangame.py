import random
# List of 5 predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]
# Select a random word
word = random.choice(words)
# Store guessed letters
guessed_letters = []
# Maximum number of incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0
# Display the word with underscores
display_word = ["_"] * len(word)
print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")
# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    # Show current progress
    print("Word:", " ".join(display_word))
    # Show guessed letters
    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)
    # Get player's guess
    guess = input("Enter a letter: ").lower().strip()
    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue
    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue
    # Add the letter to guessed letters
    guessed_letters.append(guess)
    # Check whether the guessed letter is in the word
    if guess in word:
        print("Correct guess!\n")
        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Incorrect guess!\n")
# Game result
if "_" not in display_word:
    print("================================")
    print("🎉 CONGRATULATIONS! YOU WON!")
    print("The word was:", word)
    print("================================")
else:
    print("================================")
    print("💀 GAME OVER!")
    print("The word was:", word)
    print("================================")