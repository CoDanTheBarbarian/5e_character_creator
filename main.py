from character import *
from database.race_subrace import *
from random_stats import *
from character_sheet import *
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

def choose_stats():
    stats = get_random_stats()
    print(f"You rolled: {stats}")
    response = input("Would you like to keep these stats? If not, we'll roll again. (y/n) ")
    if response == "y":
        print("With that out of the way, let's choose a race and class!")
        print("We'll assign these stats to your character after choosing a race and class.")
        return stats
    elif response == "n":
        choose_stats()
    else:
        print("Please enter 'y' or 'n'")

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

def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    c = Character(name)
    print("First things first, let's choose your race and class.")
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
    print("Let's roll some random stats.")
    stats = choose_stats()
    print("Let's assign these stats to your character, one by one.")
    assign_stats(c, stats)
    c.apply_race_bonus(race_data)
    if c.subrace != None:
        c.apply_subrace_bonus(sub_race_data)
    # c.apply_class(class_data)
    print("Creating character sheet...")
    c_data = parse_character_sheet_data(c)
    fillpdfs.write_fillable_pdf(template_path, output_path + c.name + ".pdf", c_data)
    print("Character sheet created! Check your output folder for the PDF. It will be titled the name of your character.")
    

if __name__ == "__main__":
    main()