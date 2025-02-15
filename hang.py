import random

def choose_word():
    words = ["python", "javascript", "hangman", "developer", "programming", "frontend", "backend"]
    return random.choice(words)

def display(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good job! That letter is in the word.")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                return
        else:
            attempts -= 1
            print("Wrong guess!")
    
    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
