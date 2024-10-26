from character_objects import *
from database.race_database import *
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

def choose_race():
    for i, race in enumerate(races.keys()):
        print(f"{i + 1}: {race}")
    choice = input("Choose a race: ")
    for i, race in enumerate(races.keys()):
        if choice == str(i + 1):
            confirm = input(f"You chose {race}. Is this correct? (y/n) ")
            if confirm == "y":
                stats = race_stats[race]
                race_obj = Race(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6])
                return race_obj
            elif confirm == "n":
                choose_race()
            else:
                print("Please enter 'y' or 'n'")
                choose_race()
def choose_subrace(list):
    for i, race in enumerate(list):
        print(f"{i + 1}: {race}")
    choice = input("Choose a subrace: ")
    for i, sub_race in enumerate(list):
        if choice == str(i + 1):
            confirm = input(f"You chose {race}. Is this correct? (y/n) ")
            if confirm == "y":
                stats = sub_race_stats[sub_race]
                subrace_obj = SubRace(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])
                return subrace_obj
            elif confirm == "n":
                choose_subrace(list)
            else:
                print("Please enter 'y' or 'n'")
                choose_subrace(list)
    
def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    character = Character(name)
    print("Before anything else, let's roll some random stats!")
    stats = get_random_stats()
    choose_stats(stats)
    print("Choose your race:")
    race = choose_race()
    character.apply_race_bonus(race)
    if len(character.subraces) > 0:
        sub_race = choose_subrace(character.subraces)
        character.apply_subrace_bonus(sub_race)
    
    

if __name__ == "__main__":
    main()