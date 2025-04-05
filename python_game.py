# Import the random module to generate random numbers
import random

def guessing_game():
    """Plays a simple number guessing game."""

    # Generate a random integer between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    guesses = 0
    
    # Variable to store the user's guess, initialized to None
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        # Prompt the user for their guess
        try:
            # Read the user's input as a string
            user_input = input("Enter your guess: ")
            # Convert the input to an integer
            guess = int(user_input)
            
            # Increment the guess counter
            guesses += 1

            # Compare the guess to the secret number and provide feedback
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Correct guess - print congratulatory message and exit loop
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {guesses} guesses.")
        
        except ValueError:
            # Handle cases where the input is not a valid integer
            print("Invalid input. Please enter a whole number.")

# --- Main execution ---
if __name__ == "__main__":
    # Call the main game function when the script is run directly
    guessing_game()
