import random

print("🔐 Welcome to the Password Generator!")

# Character set for passwords
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

# User input for number and length
try:
    number = int(input('🔢 How many passwords would you like to generate? '))
    length = int(input("📏 Desired length of each password: "))
    
    print('\n🔽 Here are your generated passwords:\n')

    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(f"🛡️ {password}")
    
    print("\n✅ All passwords generated successfully! Stay safe. 🧠")

except ValueError:
    print("❌ Invalid input! Please enter numbers only. 🧮")
