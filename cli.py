from random_stats import get_random_stats
from database.race_subrace import *
from database.c_class import *
from database.stat_database import *
from database.equipment.weapon_and_armor_objects import create_weapon, create_armor

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
    try:
        num = input("Choose a race: ")
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

def get_stats(c, base_stats):
    print("How would you like to assign your stats?")
    print("1. Roll random stats")
    print("2. Point Buy")
    print("3. Manual Assignment")
    try:
        choice = int(input("Choose an option: "))
        if choice not in [1, 2, 3]:
            print("Invalid choice. Please enter a number from the list.")
            return get_stats(c, base_stats)
        if confirm_choice(f"You chose option {choice}, is that correct?", get_stats):
            if choice == 1:
                print("Let's assign these stats to your character, one by one.")
                stats = choose_stats()
                assign_stats(c, stats)
            elif choice == 2:
                point_buy(c, base_stats)
            elif choice == 3:
                manual_stats(c)
        else:
            return get_stats(c, base_stats)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_stats(c, base_stats)
    

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

pt_buy_zero_stats = {
        "strength": 8,
        "dexterity": 8,
        "constitution": 8,
        "intelligence": 8,
        "wisdom": 8,
        "charisma": 8
    }

def point_buy(c, base_stats):
    points = 27
    cost = {
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
    }
    stats = base_stats.copy()
    while points > 0:
        print(f"You have {points} points to spend.")
        print("Your stats are:")
        for i, stat in enumerate(stats.keys()):
            print(f"{i + 1}: {stat}: {stats[stat]}")
        try:
            stat_num_index = int(input("Choose a stat to increase: "))
            if stat_num_index < 1 or stat_num_index > len(stats):
                print("Invalid choice. Please enter a number from the list.")
            else:
                ability = list(stats.keys())[stat_num_index - 1]
                if stats[ability] == 15:
                    print("You can't increase this stat any further.")
                    continue
                if cost[stats[ability] + 1] > points:
                    print("You don't have enough points to increase this stat.")
                    continue
                if confirm_choice(f"Increasing {ability} to {stats[ability] + 1} will cost {cost[stats[ability] + 1]} points.", lambda: None):
                    points -= cost[stats[ability] + 1]
                    stats[ability] += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    if confirm_choice("Your stats are:\n" + "\n".join([f"{stat}: {stats[stat]}" for stat in stats.keys()]), point_buy):
        for stat in stats.keys():
            c.assign_stat(stat, stats[stat])
    else:
        return point_buy(c, base_stats)
    
def manual_stats(c):
    options = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    choice = {}
    while True:
        def choose_stats():
            while len(options) > 0:
                print("Your unassigned stats are:")
                for i, option in enumerate(options):
                    print(f"{i + 1}: {option}")
                try:
                    stat_num_index = int(input("Choose a stat to assign: "))
                    if stat_num_index < 1 or stat_num_index > len(options):
                        print("Invalid choice. Please enter a number from the list.")
                    else:
                        ability = options[stat_num_index - 1]
                        stat = int(input(f"Assign {ability} to: "))
                        try:
                            if stat < 1 or stat > 18:
                                print("Invalid choice. Stat must be between 1 and 18.")
                            else:
                                if confirm_choice(f"Assign {ability} to {stat}?", choose_stats):
                                    choice[ability] = stat
                                    options.remove(ability)
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        choose_stats()
        if confirm_choice("Your stats are:\n" + "\n".join([f"{stat}: {choice[stat]}" for stat in choice.keys()]), manual_stats):
            for ability, stat in choice.items():
                c.assign_stat(ability, stat)
            return
        else:
            options = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            choice = {}
            return manual_stats(c)

def gain_proficiency_choices(c, list, num_choices):
    options_left = list[:]
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
    print(f"You have chosen: {', '.join(choices)}")
    while True:
        try:
            confirm = input("Confirm? (y/n) ")
            if confirm.lower() == "y":
                c.gain_proficiency(choices)
                return 
            elif confirm.lower() == "n":
                choices = []
                choices_left = num_choices
                gain_proficiency_choices(c, list, num_choices)
                return
            else:
                print("Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter a 'y' or 'n'.")

def choose_background():
    while True:
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
        except ValueError:
            print("Invalid input. Please enter a number.")
    
def add_starting_equipment_to_inventory(c, dict):
    for weapon in dict["weapons"]:
        w = create_weapon(weapon)
        c.add_to_inventory(w)
    for i, weapon in enumerate(c.inventory):
        print(f"{i + 1}: {weapon}")
    def choose_weapon():
        try:
            num = int(input("Choose a weapon to equip: "))
            if num >= 1 and num <= len(dict["weapons"]):
                c.equip_weapon(c.inventory[num - 1])
            else:
                print("Invalid weapon choice. Please enter a valid number.")
                return choose_weapon()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return choose_weapon()
    choose_weapon()

    for armor in dict["armor"]:
        a = create_armor(armor)
        c.add_to_inventory(a)
        if a.name == "shield":
            c.equip_shield(a)
        else:
            c.equip_armor(a)

def choose_fighting_style(self):
        styles = class_option_data[self.class_name][fighting_style]
        for i, style in enumerate(styles.keys(), start=1):
            print(f"{i}. {style}: {styles[style]}")
        try:
            num = int(input("Select a fighting style: "))
            if num > 0 and num <= len(styles):
                if confirm_choice(f"Is {num} correct?", choose_fighting_style):
                    style_name = list(styles.keys())[num - 1]
                    self.class_info[fighting_style] = style_name
                    self.class_abilities[style_name] = styles[style_name]
                    return
                else:
                    choose_fighting_style()
            else:
                print("Invalid choice.")
                choose_fighting_style()
        except ValueError:
            print("Invalid input. Please enter a number.")
            choose_fighting_style()

def choose_favored_enemy(self):
        enemies = class_option_data[self.class_name][favored_enemy]
        for i, enemy in enumerate(enemies):
            print(f"{i + 1}. {enemy}")
        try:
            num = int(input("Select a favored enemy: "))
            if num > 0 and num <= len(enemies):
                if confirm_choice(f"Is {num} correct?", choose_favored_enemy):
                    self.class_abilities[favored_enemy] = enemies[num - 1]
                    return
                else:
                    choose_favored_enemy()
            else:
                print("Invalid choice.")
                choose_favored_enemy()
        except ValueError:
            print("Invalid input. Please enter a number.")
            choose_favored_enemy()

def choose_favored_terrain(self):
        terrains = class_option_data[self.class_name][favored_terrain]
        for i, terrain in enumerate(terrains):
            print(f"{i + 1}. {terrain}")
        try:
            num = int(input("Select a favored terrain: "))
            if num > 0 and num <= len(terrains):
                if confirm_choice(f"Is {num} correct?", choose_favored_terrain):
                    self.class_abilities[favored_terrain] = terrains[num - 1]
                    return
                else:
                    choose_favored_terrain()
            else:
                print("Invalid choice.")
                choose_favored_terrain()
        except ValueError:
            print("Invalid input. Please enter a number.")
            choose_favored_terrain()

def choose_sorcerous_origin(self):
        origins = class_option_data[self.class_name][origin]
        for i, name in enumerate(origins.keys()):
            print(f"{i + 1}. {name}")
        try:
            num = int(input("Select a sorcerous origin: "))
            if num > 0 and num <= len(origins):
                if confirm_choice(f"Is {num} correct?", choose_sorcerous_origin):
                    origin_name = list(origins.keys())[num - 1]
                    if origin_name == "Wild Magic":
                        self.class_abilities[origin] = origin_name
                        for ability in origins[origin_name]:
                            self.class_abilities[ability] = origins[origin_name][ability]
                    elif origin_name == "Draconic Bloodline":
                        for i, color in enumerate(origins[origin_name]):
                            print(f"{i + 1}. {color} - Damage Resistance: {origins[origin_name][color]}")
                        try:
                            num = int(input("Select a draconic color: "))
                            if num > 0 and num <= len(origins[origin_name]):
                                if confirm_choice(f"Is {num} correct?", choose_sorcerous_origin):
                                    color_name = list(origins[origin_name].keys())[num - 1]
                                    damage_resist = origins[origin_name][color_name]
                                    self.class_abilities[origin] = origin_name
                                    self.class_abilities[origin_name] = color_name
                                    self.class_abilities["Draconic Resistance"] = damage_resist
                                    return
                                else:
                                    choose_sorcerous_origin()
                            else:
                                print("Invalid choice.")
                                choose_sorcerous_origin()
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            choose_sorcerous_origin()
                    return
                else:
                    choose_sorcerous_origin()
            else:
                print("Invalid choice.")
                choose_sorcerous_origin()
        except ValueError:
            print("Invalid input. Please enter a number.")
            choose_sorcerous_origin()

def choose_patron(self):
        patrons = class_option_data[self.class_name][patron]
        for i, name in enumerate(patrons):
            print(f"{i + 1}. {name}")
        try:
            num = int(input("Select a patron: "))
            if num > 0 and num <= len(patrons):
                if confirm_choice(f"Is {num} correct?", choose_patron):
                    patron_name = list(patrons.keys())[num - 1]
                    self.class_abilities[patron] = patron_name
                    for i, ability in enumerate(patrons[patron_name]):
                        self.class_abilities[ability] = patrons[patron_name][ability]
                    return
                else:
                    choose_patron()
            else:
                print("Invalid choice.")
                choose_patron()
        except ValueError:
            print("Invalid input. Please enter a number.")
            choose_patron()

def make_class_choices(self):
    if self.class_name == "Cleric":
        pass
    elif self.class_name == "Fighter":
        choose_fighting_style(self)
    elif self.class_name == "Ranger":
        choose_favored_terrain(self)
        choose_favored_enemy(self)
    elif self.class_name == "Sorcerer":
        choose_sorcerous_origin(self)
    elif self.class_name == "Warlock":
        choose_patron(self)
