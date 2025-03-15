import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: Easy (E), Medium (M), Hard (H)")
    
    difficulty = input("Enter E, M, or H: ").strip().lower()
    
    if difficulty == 'e':
        max_number = 50
        max_attempts = None  # Unlimited
    elif difficulty == 'm':
        max_number = 100
        max_attempts = 10
    elif difficulty == 'h':
        max_number = 200
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        max_number = 100
        max_attempts = 10

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"Guess the number between 1 and {max_number}. Type 'exit' to quit.")

    while True:
        user_input = input("Enter your guess: ").strip()

        if user_input.lower() == "exit":
            print(f"The secret number was {secret_number}. Thanks for playing!")
            break

        try:
            guess = int(user_input)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
            
            if max_attempts and attempts >= max_attempts:
                print(f"❌ Out of attempts! The correct number was {secret_number}.")
                break
                
        except ValueError:
            print("Invalid input! Please enter a number or type 'exit' to quit.")

if __name__ == "__main__":
    number_guessing_game()

    while True:
        number_guessing_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! 👋")
            break

