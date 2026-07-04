import random

def hangman():
    words = ["python", "github", "coding", "tracker", "chatbot"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
                
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break
            
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess.")
            guessed_letters.append(guess)
            attempts -= 1
            
    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
    