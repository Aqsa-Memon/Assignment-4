
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = None
    
    print(f"\n🎯 Welcome to the Guessing Game! Guess a number between 1 and {x}.\n")
    
    while guess != random_number:
        try:
            guess = int(input("🔢 Your guess: "))
            if guess < 1 or guess > x:
                print(f"⚠️ Please guess a number *between* 1 and {x}.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue
        
        if guess < random_number:
            print("📉 Too low. Try again!\n")
        elif guess > random_number:
            print("📈 Too high. Try again!\n")

    print(f"\n🎉 Congrats! You guessed the number {random_number} correctly!\n")

# Start the game
guess(10)
