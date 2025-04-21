import random

def play_rps():
    item_list = ["rock", "paper", "scissor"]

    user_input = input("Enter your move (Rock, Paper, Scissor): ").lower()
    comp_choice = random.choice(item_list)

    if user_input not in item_list:
        print("❌ Invalid move! Please choose Rock, Paper, or Scissor.")
        return

    print(f"\n🧍‍♂️ You chose: {user_input.capitalize()} \n💻 Computer chose: {comp_choice.capitalize()}")

    if user_input == comp_choice:
        print("🤝 It's a tie!")

    elif user_input == "rock":
        if comp_choice == "paper":
            print("📄 Paper covers Rock — Computer wins!")
        else:
            print("🪨 Rock smashes Scissor — You win!")

    elif user_input == "paper":
        if comp_choice == "scissor":
            print("✂️ Scissor cuts Paper — Computer wins!")
        else:
            print("📄 Paper covers Rock — You win!")

    elif user_input == "scissor":
        if comp_choice == "rock":
            print("🪨 Rock smashes Scissor — Computer wins!")
        else:
            print("✂️ Scissor cuts Paper — You win!")

# Start the game
play_rps()
