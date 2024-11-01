import pytest
from c_class import *

def test_get_class_data():
    class_input = "Barbarian"
    data = class_data[class_input]
    assert data[class_name] == "Barbarian"
    assert data[hit_die] == 12
    assert data[proficiencies] == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert data[prof_choices] == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert data[class_info] == {
        "Unarmored Defense": "While you are not wearing any armor, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "Rage": "During your turn in combat, you can rage as a bonus action. While raging you gain the following benefits:\n - You have advantage of Stregth checks and saving throws\n - When you make a strength based weapon attack add 2 to your attack roll\n - You have resistance to bludgeoning, piercing, and slashing damage\nYou can't cast spells while raging. Your rage lasts for 1 minute and ends if you are knocked unconscious or you haven't attacked a hostile creature since your last turn."
    }
    assert data[equipment] == {
            "weapons": ["great axe", "halberd", "javelin"],
            "armor": [],
        }
    assert data[class_abilities] == {"Rage Charges": 2}

def test_get_class_creator():
    class_input = "Barbarian"
    func = class_create_map[class_input]
    assert func == create_barbarian

    class_input = "Bard"
    func = class_create_map[class_input]
    assert func == create_bard

    class_input = "Cleric"
    func = class_create_map[class_input]
    assert func == create_cleric

    class_input = "Druid"
    func = class_create_map[class_input]
    assert func == create_druid

    class_input = "Fighter"
    func = class_create_map[class_input]
    assert func == create_fighter

    class_input = "Monk"
    func = class_create_map[class_input]
    assert func == create_monk

    class_input = "Paladin"
    func = class_create_map[class_input]
    assert func == create_paladin

    class_input = "Ranger"
    func = class_create_map[class_input]
    assert func == create_ranger

    class_input = "Rogue"
    func = class_create_map[class_input]
    assert func == create_rogue

    class_input = "Sorcerer"
    func = class_create_map[class_input]
    assert func == create_sorcerer

    class_input = "Warlock"
    func = class_create_map[class_input]
    assert func == create_warlock

    class_input = "Wizard"
    func = class_create_map[class_input]
    assert func == create_wizard

def test_create_class_handler():
    class_input = "Barbarian"
    barb = create_class_object(class_input)
    assert barb.class_name == "Barbarian"
    assert barb.hit_die == 12
    assert barb.proficiencies == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert barb.prof_choice == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert barb.class_info == {
        "Unarmored Defense": "While you are not wearing any armor, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "Rage": "During your turn in combat, you can rage as a bonus action. While raging you gain the following benefits:\n - You have advantage of Stregth checks and saving throws\n - When you make a strength based weapon attack add 2 to your attack roll\n - You have resistance to bludgeoning, piercing, and slashing damage\nYou can't cast spells while raging. Your rage lasts for 1 minute and ends if you are knocked unconscious or you haven't attacked a hostile creature since your last turn."
    }
    assert barb.starting_equipment == {
            "weapons": ["great axe", "halberd", "javelin"],
            "armor": [],
        }
    assert barb.class_abilities == {"Rage Charges": 2}

def test_create_barb():
    barb = create_barbarian(class_data["Barbarian"])
    assert barb.class_name == "Barbarian"
    assert barb.hit_die == 12
    assert barb.proficiencies == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert barb.prof_choice == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert barb.class_info == {
        "Unarmored Defense": "While you are not wearing any armor, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "Rage": "During your turn in combat, you can rage as a bonus action. While raging you gain the following benefits:\n - You have advantage of Stregth checks and saving throws\n - When you make a strength based weapon attack add 2 to your attack roll\n - You have resistance to bludgeoning, piercing, and slashing damage\nYou can't cast spells while raging. Your rage lasts for 1 minute and ends if you are knocked unconscious or you haven't attacked a hostile creature since your last turn."
    }
    assert barb.starting_equipment == {
            "weapons": ["great axe", "halberd", "javelin"],
            "armor": [],
        }
    assert barb.class_abilities == {"Rage Charges": 2}


