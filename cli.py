from random_stats import *
from database.race_subrace import *
from database.c_class import *
from database.stat_database import *

def parse_name(name):
    response = input("Character name: " + name + "\nConfirm? (y/n) ")
    if response == "n":
        name = input("What is your new character's name?\n")
        parse_name(name)
    elif response == "y":
        print(f"Excellent! Marking {name} to your character sheet.")
    else:
        print("Please enter 'y' or 'n'")
        parse_name(name)

def confirm_choice(choice_description, callback):
    while True:
        response = input(f"{choice_description}\nConfirm? (y/n) ")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False  # Return False to indicate a "no" confirmation
        else:
            print("Please enter 'y' or 'n'.")
def choose_race():
    for i, race in enumerate(races.keys()):
        print(f"{i + 1}: {race}")
    num = input("Choose a race: ")
    try:
        num = int(num)
        if 1 <= num <= len(races):
            race = list(races.keys())[num - 1]
            if confirm_choice(f"Is {race} correct?", choose_race):
                return race
        else:
            print("Invalid race choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return choose_race()

def choose_subrace(list):
    for i, subrace in enumerate(list):
        print(f"{i + 1}: {subrace}")
    try:
        num = int(input("Choose a subrace: "))
        if 1 <= num <= len(list):
            subrace = list[num - 1]
            if confirm_choice(f"Is {subrace} correct?", choose_subrace):
                return subrace
        else:
            print("Invalid subrace choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return choose_subrace(list)

def choose_class():
    for i, c in enumerate(class_data.keys()):
        print(f"{i + 1}: {c}")
    try:
        num = input("Choose a class: ")
        if num.isdigit() and 1 <= int(num) <= len(class_data):
            c = list(class_data.keys())[int(num) - 1]
            if confirm_choice(f"Is {c} correct?", choose_class):
                return c
        else:
            print("Invalid class choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return choose_class()

def choose_stats():
    while True:
        stats = get_random_stats()
        if confirm_choice(f"You rolled: {stats}\nWould you like to keep these stats? If not, we'll roll again.", lambda: None):
            return stats


def assign_stats(c, stats):
    options = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    while len(options) > 0:
        print("Your stats are:")
        for i, stat in enumerate(stats):
            print(f"{i + 1}: {stat}")
        try:
            stat_num_index = int(input("Choose a stat to assign: "))
            if stat_num_index < 1 or stat_num_index > len(stats):
                print("Invalid choice. Please enter a number from the list.")
            else:
                print(f"Assigning: {stats[stat_num_index - 1]}")
                print("Remaining unassigned core stats:")
                for i, option in enumerate(options):
                    print(f"{i + 1}: {option}")
                stat_index = int(input("Choose a core stat to assign to: "))
                if stat_index < 1 or stat_index > len(options):
                    print("Invalid choice. Please enter a number from the list.")
                else:
                    c.assign_stat(options[stat_index - 1], stats[stat_num_index - 1])
                    options.remove(options[stat_index - 1])
                    stats.remove(stats[stat_num_index - 1])
        except ValueError:
            print("Invalid input. Please enter a number.")

def gain_proficiency_choices(c, list, num_choices):
    options_left = list[:]  # create a copy of the list
    choices = []
    choices_left = num_choices

    while choices_left > 0:
        for i, option in enumerate(options_left):
            print(f"{i + 1}: {option}")
        print(f"You have {choices_left} choices left.")
        try:
            choice_num = int(input("Choose a skill: "))
            if choice_num < 1 or choice_num > len(options_left):
                print("Invalid choice. Please enter a number from the list.")
            else:
                print(f"Chosen skill: {options_left[choice_num - 1]}")
                choices.append(options_left[choice_num - 1])
                options_left.pop(choice_num - 1)  # remove chosen option from list
                choices_left -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    while choices_left == 0:
        print(f"You have chosen: {', '.join(choices)}")
        try:
            confirm = input("Confirm? (y/n) ")
            if confirm.lower() == "y":
                c.gain_proficiency(choices)
                break
            elif confirm.lower() == "n":
                gain_proficiency_choices(c, list, num_choices)
            else:
                print("Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter a 'y' or 'n'.")

def choose_background():
    for i, background in enumerate(backgrounds.keys()):
        print(f"{i + 1}: {background}. Proficiencies: {backgrounds[background]}")
    try:
        num = input("Choose a background: ")
        if num.isdigit() and 1 <= int(num) <= len(backgrounds):
            b = list(backgrounds.keys())[int(num) - 1]
            if confirm_choice(f"Chosen background: {b}", choose_background):
                return b
        else:
            print("Invalid background choice. Please enter a valid number.")
            return choose_background()
    except ValueError:
        print("Invalid input. Please enter a number.")
    return choose_background