import random

# List of words
words = ["python", "streamlit", "mobile"]

# Randomly select a word
word = random.choice(words)

# Initialize game variables
total_chances = 7
guessed_word = "-" * len(word)

print("\n🔤 Welcome to the Word Guessing Game!")
print("🧠 Try to guess the word one letter at a time!\n")

# Main game loop
while total_chances != 0:
    print(f"🔎 Word: {guessed_word}")
    letter = input("✏️ Guess a letter: ").lower()  # Convert input to lowercase to match the word

    if letter in word:
        # Update guessed_word with the correctly guessed letter
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]

        # Check if the word is fully guessed
        if guessed_word == word:
            print(f"\n🎉 Congratulations! You won!!! The word was: **{word}** 🏆")
            break
        else:
            print("✅ Good guess!\n")
    else:
        total_chances -= 1
        print("❌ Incorrect guess.")
        print(f"💡 Remaining chances: {total_chances}\n")

# Check if the player lost
if guessed_word != word:
    print("\n💀 Game over.")
    print("😢 You lose.")
    print("📉 All the chances are exhausted.")
    print(f"✅ The correct word was: **{word}**")
