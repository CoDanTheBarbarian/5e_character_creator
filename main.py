from character import *
from database.race_subrace import *
from random_stats import *
from pdf.character_sheet import *
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
    response = input("Would you like to roll again? If not, we'll keep these stats. (y/n) ")
    if response == "y":
        stats = get_random_stats()
        choose_stats(stats)
    elif response == "n":
        print("With stats out of the way, let's choose a race and class!")
        print("We'll assign stats later.")
    else:
        print("Please enter 'y' or 'n'")
        choose_stats(stats)

def assign_stats(c, stats):
    options = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    while len(options) > 0:
        print("Your stats are:")
        for i, stat in enumerate(stats):
            print(f"{i + 1}: {stat}")
        stat_num_index = int(input("Choose a stat to assign: "))
        if stat_num_index > 0 and stat_num_index <= len(stats):
            continue
        else:
            print("Invalid choice. Please enter a number from the list.")
        print(f"Assigning {stat[i - 1]}")
        print("Remaining unassigned core stats:")
        for i, option in enumerate(options):
            print(f"{i + 1}: {option}")
        stat_index = input("Choose a core stat to assign: ")
        if stat_index > 0 and stat_index <= len(options):
            continue
        else:
            print("Invalid choice. Please enter a number from the list.")
        c.assign_stat(stats[stat_num_index - 1], options[stat_index - 1])
        options.remove(options[stat_index - 1])
        stats.remove(stats[stat_num_index - 1])

    


def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    c = Character(name)
    print("Before anything else, let's roll some random stats!")
    stats = get_random_stats()
    choose_stats(stats)
    print("Choose your race:")
    race_choice = get_race_input()
    race_data = create_race_object(race_choice)
    if len(race_data.subraces) > 0:
        print("Looks like you have some options for a subrace.")
        sub_race_choice = get_subrace_input(race_data.subraces)
        if c.race == "Dragonborn":
            sub_race_data = create_dragoncolor_object(sub_race_choice)
        else:
            sub_race_data = create_subrace_object(sub_race_choice)
    
    # grab a class and create a class object

    # assign_stats(c, stats) <-- not functioning properly
    c.apply_race_bonus(race_data)
    if c.subrace != None:
        c.apply_subrace_bonus(sub_race_data)
    print("Creating character sheet...")
    c_data = parse_character_sheet_data(c)
    fillpdfs.write_fillable_pdf(template_path, output_path + c.name + ".pdf", c_data)
    print("Character sheet created! Check your output folder for the PDF. It will be titled the name of your character.")
    

if __name__ == "__main__":
    main()