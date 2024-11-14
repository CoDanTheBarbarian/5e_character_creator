from character import *
from database.race_subrace import *
from database.c_class import *
from database.equipment.weapon_and_armor_objects import *
from random_stats import *
from character_sheet import *
from cli import *
from fillpdf import fillpdfs
import os
import sys
import time

base_dir = os.path.dirname(__file__)
template_path = os.path.join(os.path.dirname(__file__), "pdf", "Character_Sheet_Template.pdf")
output_path = os.path.join(base_dir, "pdf", "character_pdfs/")
if getattr(sys, 'frozen', False):
    # The application is frozen
    template_path = os.path.join(sys._MEIPASS, "Character_Sheet_Template.pdf")
    output_path = ""


def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    c = Character(name)
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
    make_class_choices(c, class_obj)
    get_stats(c, pt_buy_zero_stats)
    print("Choose a background for your character:")
    background = choose_background()
    print("Updating character sheet with your race and class choices.")
    c.apply_race_bonus(race_obj)
    if race_obj.prof_choices:
        print("Looks like you have some options for skill proficiencies to gain from your race.")
        gain_proficiency_choices(c, race_obj.prof_choices[0], race_obj.prof_choices[1])
    if subrace_obj != None:
        c.apply_subrace_bonus(subrace_obj)
    if class_obj.prof_choice:
        print("Looks like you have some options for skill proficiencies to gain from your class.")
        gain_proficiency_choices(c, class_obj.prof_choice[0], class_obj.prof_choice[1])
    c.apply_class(class_obj)
    add_starting_equipment_to_inventory(c, class_obj.starting_equipment)
    c.apply_background(background)
    c.unarmored_ac()
    c.hp = c.get_starting_hp()
    print("Creating character sheet...")
    c_data = parse_character_sheet_data(c)
    if output_path == "":
        fillpdfs.write_fillable_pdf(template_path, c.name + ".pdf", c_data)
    else:
        fillpdfs.write_fillable_pdf(template_path, output_path + c.name + ".pdf", c_data)
    print(f"Character sheet created! Your character sheet is located in {output_path}.")
    print("Thanks for using my character creator!")
    i = 3
    while i > 0:
        print(f"Closing in {i} seconds...")
        time.sleep(1)
        i -= 1

if __name__ == "__main__":
    main()