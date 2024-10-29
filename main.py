from character import *
from database.race_subrace import *
from database.c_class import *
from random_stats import *
from character_sheet import *
from cli import *

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
        if race_data.race == "dragonborn":
            sub_race_data = create_dragoncolor_object(sub_race_choice)
        else:
            sub_race_data = create_subrace_object(sub_race_choice)
    class_name = get_class_input()
    class_data = create_class_object(class_name)
    
    print("Let's roll some random stats.")
    stats = choose_stats()
    print("Let's assign these stats to your character, one by one.")
    assign_stats(c, stats)
    print("Let's update your character sheet with your race and class choices.")
    c.apply_race_bonus(race_data)
    if c.subrace != None:
        c.apply_subrace_bonus(sub_race_data)
    c.apply_class(class_data)
    print("Creating character sheet...")
    c_data = parse_character_sheet_data(c)
    fillpdfs.write_fillable_pdf(template_path, output_path + c.name + ".pdf", c_data)
    print(f"Character sheet created! Your character sheet is located in {output_path}.")
    

if __name__ == "__main__":
    main()