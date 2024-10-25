from character.character_objects import *
from random_stats import *
def parse_name(name):
    response = input("Character name: " + name + "\nConfirm? (y/n) ")
    if response == "n":
        name = input("What is your new character's name? ")
        parse_name(name)
    elif response == "y":
        print(f"Excellent! Marking {name} to your character sheet.")
    else:
        print("Please enter 'y' or 'n'")
        parse_name(name)

def choose_stats(stats):
    print(f"You rolled: {stats}")
    response = input("Would you like to roll again? (y/n) ")
    if response == "y":
        stats = get_random_stats()
        choose_stats(stats)
    elif response == "n":
        print("With stats out of the way, let's choose a race and class!")
        print("We'll assign stats later.")
    else:
        print("Please enter 'y' or 'n'")
        choose_stats(stats)


def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    character = Character(name)
    print("Before anything else, let's roll some random stats!")
    stats = get_random_stats()
    choose_stats(stats)
    print("Choose your race:")
    
if __name__ == "__main__":
    main()