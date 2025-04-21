import time

def countdown_timer(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        # Timer format (MM:SS)
        timer = f'{mins:02}:{secs:02}'
        print(f"\r⌛ Counting down: {timer} ⏳", end="")  # Live countdown
        time.sleep(1)
        seconds -= 1

    print("\n\n🚨 Ding ding! Time's up! ⏰🎉")

try:
    total_seconds = int(input("🔢 Enter time in seconds for the countdown: "))
    print("🔽 Starting countdown...\n")
    countdown_timer(total_seconds)
except ValueError:
    print("❌ Invalid input! Please enter a valid number (digits only). 🧮")
