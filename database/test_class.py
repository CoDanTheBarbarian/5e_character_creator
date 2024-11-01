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
    barb = create_class_object("Barbarian")
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

def test_create_ranger():
    data = class_data["Ranger"]
    assert data[class_name] == "Ranger"
    assert data[hit_die] == 10
    assert data[proficiencies] == ["light armor",
                                   "medium armor",
                                   "heavy armor",
                                   "shield",
                                   "simple weapons",
                                   "martial weapons",
                                   "strength",
                                   "dexterity"]
    assert data[prof_choices] == (["animal handling", "athletics", "insight", "investigation", "nature", "perception", "stealth", "survival"], 3)
    assert data[class_info] == {
        "Favored Enemy": "You have advantage on Survival checks to track your favored enemy and on Intelligence checks to recall information about them.",
        "Natural Explorer": "While in your favored terrain, when you make Intelligence and Wisdom checks related to that terrain, your proficiency bonus is doubled if applicable.\nWhile traveling for an hour or more in your favored terrain you gain the following benefits:\n - Unaffected by difficult terrain\n - Can't get lost except by magical means\n - Move stealthily at a normal pace"
    }
    assert data[equipment] == {
            "weapons": ["short sword", "short sword", "long bow"],
            "armor": ["ring mail"],
        }
    assert data[class_abilities] == {"Favored Terrain": None, "Favored Enemy": None}
    assert data[spell_casting_ability] == None
    assert data[spell_slots] == None
    assert data[spells_known] == None
    c = create_class_object("Ranger")
    assert c.class_name == "Ranger"
    assert c.hit_die == 10

def test_draconic_resistance():
    data = {
        class_name: "Sorcerer",
        hit_die: 6,
        proficiencies: [
            'dagger', 
            'dart', 
            'sling', 
            'quarterstaff', 
            'light crossbow', 
            'constitution', 
            'charisma'
        ],
        prof_choices: (
            [
                "deception", 
                "insight", 
                "intimidation", 
                "persuasion", 
                "religion"
            ], 2
        ),
        class_info: class_abil_desc["Sorcerer"],
        equipment: {
            "weapons": ["quarterstaff", "light crossbow", "dagger", "dagger"],
            "armor": [],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 2,
        class_abilities: {
            origin: "Draconic Bloodline",
            "Draconic Bloodline": "Black"
                          },
        }
    c = Class(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known]
        )
    
    assert c.class_abilities[origin] == "Draconic Bloodline"
    assert c.class_abilities["Draconic Bloodline"] == "Black"
    color = c.class_abilities["Draconic Bloodline"]
    assert color == "Black"
    assert class_option_data["Sorcerer"]["Sorcerous Origin"]["Draconic Bloodline"][color] == "Acid"
    assert class_option_data["Sorcerer"]["Sorcerous Origin"]["Draconic Bloodline"][color].lower() == "acid"