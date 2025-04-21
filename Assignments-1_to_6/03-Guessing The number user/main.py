import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print(f"\n🤖 Think of a number between 1 and {x}, and I'll try to guess it!")
    print("Tell me if my guess is: (H)igh, (L)ow, or (C)orrect.\n")
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one number left
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback not in ['h', 'l', 'c']:
            print("⚠️ Please enter a valid response: H, L, or C.\n")
            continue

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"\n🎉 Yay! I guessed your number — it was {guess}! Thanks for playing!\n")

# Start the game
computer_guess(10)
