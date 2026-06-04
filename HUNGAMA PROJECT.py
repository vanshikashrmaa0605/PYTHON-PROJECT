import random

def play_hangman():
    # 1. Predefined list of 5 words
    word_list = ["python", "software", "intern", "script", "automation"]
    
    # Randomly select a word from the list
    secret_word = random.choice(word_list)
    
    # Track letters that the player has guessed
    guessed_letters = []
    
    # Limit incorrect guesses to 6
    incorrect_guesses_left = 6

    print("--- Welcome to Hangman! ---")
    print("Try to guess the secret word one letter at a time.")
    print(f"You can make up to {incorrect_guesses_left} incorrect guesses.")
    print("---------------------------\n")

    # Game loop runs as long as the player has attempts left
    while incorrect_guesses_left > 0:
        
        # 2. Display the current word progress (e.g., p _ t h o n)
        displayed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        
        print(f"Word: {displayed_word.strip()}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the player has guessed all the letters
        # (Stripping spaces out of our displayed word to match secret_word)
        if "_" not in displayed_word:
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
            break

        # 3. Get console input from the player
        guess = input("\nGuess a letter: ").lower().strip()

        # 4. Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one.")
            continue

        # Add the valid guess to our tracking list
        guessed_letters.append(guess)

        # 5. Check if the guess is right or wrong using if-else logic
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # 6. Game over condition
    if incorrect_guesses_left == 0:
        print("\n💥 Game Over! You ran out of guesses.")
        print(f"The secret word was: '{secret_word}'")

# Run the game
if __name__ == "__main__":
    play_hangman()
    
