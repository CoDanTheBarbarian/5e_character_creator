from random_stats import *
from database.race_subrace import *

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
            return callback()  # Re-run the callback if choice is denied
        else:
            print("Please enter 'y' or 'n'.")

def get_race_input():
    for i, race in enumerate(races.keys()):
        print(f"{i + 1}: {race}")
    def select_race():
        num = input("Choose a race: ")
        if num.isdigit() and 1 <= int(num) <= len(races):
            race = list(races.keys())[int(num) - 1]
            if confirm_choice(f"Is {race} correct?", select_race):
                return race
        else:
            print("Invalid race choice. Please enter a valid number.")
        return select_race()
    return select_race()

def get_subrace_input(list):
    for i, subrace in enumerate(list):
        print(f"{i + 1}: {subrace}")
    def select_subrace():
        num = input("Choose a race: ")
        if num.isdigit() and 1 <= int(num) <= len(list):
            subrace = list[int(num) - 1]
            if confirm_choice(f"Is {subrace} correct?", select_subrace):
                return subrace
        else:
            print("Invalid subrace choice. Please enter a valid number.")
        return select_subrace()
    return select_subrace()

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