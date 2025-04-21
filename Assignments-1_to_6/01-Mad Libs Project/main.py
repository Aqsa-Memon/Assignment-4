import random

def mad_libs_story_1():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")

    story = f"""
    It was a {adjective} day. I saw a {noun} that {verb} {adverb} down the street.
    People were amazed and started clapping. What a sight!
    """
    return story


def mad_libs_story_2():
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    food = input("Enter a food item: ")
    emotion = input("Enter an emotion: ")

    story = f"""
    One day, {name} went to {place} to eat some {food}.
    Suddenly, they felt very {emotion} and decided to dance in public.
    Everyone joined in, and it became a viral video!
    """
    return story


def mad_libs_story_3():
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    object = input("Enter an object: ")
    silly_word = input("Enter a silly word: ")

    story = f"""
    Once upon a time, a {color} {animal} found a magical {object}.
    When it touched it, the animal shouted, "{silly_word}!" and disappeared.
    No one ever saw it again.
    """
    return story


def choose_story():
    print("Welcome to Mad Libs! Choose a story:\n")
    print("1. A Day on the Street")
    print("2. The Viral Dance")
    print("3. The Magical Animal")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nYour story:\n", mad_libs_story_1())
    elif choice == "2":
        print("\nYour story:\n", mad_libs_story_2())
    elif choice == "3":
        print("\nYour story:\n", mad_libs_story_3())
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    choose_story()
    print("\nThanks for playing Mad Libs!")