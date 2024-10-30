from character import *
from database.race_subrace import *
from database.c_class import *
from database.equipment.weapon_and_armor_objects import *
from random_stats import *
from character_sheet import *
from cli import *
from fillpdf import fillpdfs

def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    c = Character(name)
    print("First things first, let's choose your race and class.")
    print("Choose your race:")
    race_choice = choose_race()
    race_obj = create_race_object(race_choice)
    subrace_obj = None
    if len(race_obj.subraces) > 0:
        print("Looks like you have some options for a subrace.")
        print("Choose your subrace:")
        sub_race_choice = choose_subrace(race_obj.subraces)
        if race_obj.race == "Dragonborn":
            subrace_obj = create_dragoncolor_object(sub_race_choice)
        else:
            subrace_obj = create_subrace_object(sub_race_choice)
    print("Choose your class:")
    class_name = choose_class()
    class_obj = create_class_object(class_name)
    get_stats(c, pt_buy_zero_stats)
    print("Let's update your character sheet with your race and class choices.")
    c.apply_race_bonus(race_obj)
    if subrace_obj != None:
        c.apply_subrace_bonus(subrace_obj)
    c.apply_class(class_obj)
    add_starting_equipment_to_inventory(c, class_obj.starting_equipment)
    print("Let's choose a background for your character.")
    background = choose_background()
    c.apply_background(background)
    print("Creating character sheet...")
    c_data = parse_character_sheet_data(c)
    fillpdfs.write_fillable_pdf(template_path, output_path + c.name + ".pdf", c_data)
    print(f"Character sheet created! Your character sheet is located in {output_path}.")
    print("Thanks for using my character creator!")
    print("Character Object:")
    print(c)

    

if __name__ == "__main__":
    main()