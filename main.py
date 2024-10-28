from character import *
from database.race_subrace import *
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
    if race_data.prof_choices != []:
        print("Looks like you have some options for skill proficiencies to gain.")
        gain_proficiency_choices(c, race_data.prof_choices[0][0], race_data.prof_choices[0][1])
    if len(race_data.subraces) > 0:
        print("Looks like you have some options for a subrace.")
        sub_race_choice = get_subrace_input(race_data.subraces)
        if c.race == "Dragonborn":
            sub_race_data = create_dragoncolor_object(sub_race_choice)
        else:
            sub_race_data = create_subrace_object(sub_race_choice)
    
    # grab a class and create a class object
    print("Let's roll some random stats.")
    stats = roll_stats()
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