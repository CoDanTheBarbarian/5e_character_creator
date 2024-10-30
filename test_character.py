import pytest
from character import Character
from database.race_subrace import *
from database.equipment.weapon_and_armor_objects import create_weapon, create_armor

def test_create_character():
    c = Character("test")
    assert c.name == "test"

def test_assign_stat():
    c = Character("testing")
    assert c.strength == 8
    assert c.dexterity == 8
    assert c.constitution == 8
    assert c.intelligence == 8
    assert c.wisdom == 8
    assert c.charisma == 8
    c.assign_stat("strength", 10)
    assert c.strength == 10
    c.assign_stat("dexterity", 12)
    assert c.dexterity == 12
    c.assign_stat("constitution", 14)
    assert c.constitution == 14
    c.assign_stat("intelligence", 16)
    assert c.intelligence == 16
    c.assign_stat("wisdom", 18)
    assert c.wisdom == 18
    c.assign_stat("charisma", 20)
    assert c.charisma == 20

def test_get_saving_throw():
    c = Character("test")
    assert c.get_saving_throw("charisma") == -1
    assert c.get_saving_throw("dexterity") == -1
    assert c.get_saving_throw("constitution") == -1
    assert c.get_saving_throw("intelligence") == -1
    assert c.get_saving_throw("strength") == -1
    assert c.get_saving_throw("wisdom") == -1
    c.assign_stat("strength", 10)
    assert c.strength == 10
    assert c.get_saving_throw("strength") == 0
    c.gain_proficiency(["strength"])
    assert c.get_saving_throw("strength") == 2

def test_get_ability_mod():
    c = Character("test")
    c.strength = 15
    assert c.get_ability_mod("strength") == 2
    assert c.get_ability_mod("dexterity") == -1


def test_increase_core_stat():
    c = Character("test")
    assert c.strength == 8
    c.increase_core_stat("strength", 5)
    assert c.strength == 13

def test_decrease_core_stat():
    c = Character("test")
    assert c.strength == 8
    c.decrease_core_stat("strength", 5)
    assert c.strength == 3

def test_get_core_skill_ability():
    c = Character("testing")
    assert c.get_skill_core_ability("athletics") == "strength"
    assert c.get_skill_core_ability("perception") == "wisdom"
    assert c.get_skill_core_ability("stealth") == "dexterity"
    assert c.get_skill_core_ability("arcana") == "intelligence"
    assert c.get_skill_core_ability("intimidation") == "charisma"

def test_get_skill_bonus():
    c = Character("testing")
    assert c.get_skill_bonus("athletics") == -1
    assert c.get_skill_bonus("intimidation") == -1
    c.assign_stat("strength", 20)
    assert c.strength == 20
    assert c.get_skill_bonus("athletics") == 5
    c.assign_stat("charisma", 4)
    assert c.charisma == 4
    assert c.get_skill_bonus("intimidation") == -3

def test_get_weapon_profs():
    c = Character("testing")
    assert c.proficiencies["simple weapons"] == False
    assert c.proficiencies["martial weapons"] == False
    c.gain_proficiency(["simple weapons", "light armor"])
    assert c.get_weapon_proficiencies() == ['simple weapons', 
                  'club', 
                  'dagger', 
                  'greatclub', 
                  'handaxe', 
                  'javelin', 
                  'light hammer', 
                  'mace', 
                  'quarterstaff', 
                  'sickle', 
                  'spear', 
                  'unarmed strike', 
                  'light crossbow', 
                  'dart', 
                  'short bow', 
                  'sling',]

def test_apply_background():
    c = Character("testing")
    assert c.background == None
    c.apply_background("noble")
    assert c.background == "noble"
    assert c.proficiencies["history"] == True
    assert c.proficiencies["persuasion"] == True

    c2 = Character("testing")
    assert c2.background == None
    c2.apply_background("acolyte")
    assert c2.background == "acolyte"
    assert c2.proficiencies["insight"] == True
    assert c2.proficiencies["religion"] == True
    

def test_gain_damage_resistance():
    c = Character("testing")
    assert c.damage_resistance["acid"] == False
    c.gain_damage_resistance("acid")
    assert c.damage_resistance["acid"] == True

def test_gain_proficiency():
    c = Character("test")
    assert c.proficiencies["strength"] == False
    c.gain_proficiency(["strength"])
    assert c.proficiencies["strength"] == True
    c.gain_proficiency(["simple weapons"])
    assert c.proficiencies["simple weapons"] == True
    assert c.proficiencies["club"] == True
    assert c.proficiencies["flail"] == False
    c.gain_proficiency(["wisdom", "perception"])
    assert c.proficiencies["perception"] == True
    assert c.proficiencies["wisdom"] == True

def test_add_remove_from_inventory():
    c = Character("test")
    assert c.inventory == []
    c.add_to_inventory("test")
    assert c.inventory == ["test"]
    c.remove_from_inventory("test")
    assert c.inventory == []
    w = create_weapon("club")
    c.add_to_inventory(w)
    assert c.inventory == [w]
    w2 = create_weapon("light crossbow")
    c.add_to_inventory(w2)
    assert c.inventory == [w, w2]
    c.remove_from_inventory(w2)
    assert c.inventory == [w]
    c.remove_from_inventory(w)
    assert c.inventory == []

# def test_equip_armor():

# def test_equip_shield():

# def test_equip_weapons():

def test_apply_race_bonus():
    c = Character("test")
    assert c.strength == 8
    assert c.constitution == 8
    race_obj = create_race_object(half_orc)
    c.apply_race_bonus(race_obj)
    assert c.speed == 30
    assert c.strength == 10
    assert c.constitution == 9

    c2 = Character("testing")
    assert c2.constitution == 8
    assert c2.proficiencies["battle axe"] == False
    assert c2.proficiencies["handaxe"] == False
    assert c2.proficiencies["light hammer"] == False
    assert c2.proficiencies["warhammer"] == False
    dwarf_obj = create_race_object(dwarf)
    c2.apply_race_bonus(dwarf_obj)
    assert c2.speed == 25
    assert c2.constitution == 10
    assert c2.proficiencies["battle axe"] == True
    assert c2.proficiencies["handaxe"] == True
    assert c2.proficiencies["light hammer"] == True
    assert c2.proficiencies["warhammer"] == True
    assert c2.damage_resistance["poison"] == True

def test_apply_subrace():
    c = Character("testing")
    assert c.strength == 8
    assert c.constitution == 8
    assert c.proficiencies["battle axe"] == False
    assert c.proficiencies["handaxe"] == False
    assert c.proficiencies["light hammer"] == False
    assert c.proficiencies["warhammer"] == False
    dwarf_obj = create_race_object(dwarf)
    c.apply_race_bonus(dwarf_obj)
    assert c.speed == 25
    assert c.constitution == 10
    assert c.proficiencies["battle axe"] == True
    assert c.proficiencies["handaxe"] == True
    assert c.proficiencies["light hammer"] == True
    assert c.proficiencies["warhammer"] == True
    assert c.damage_resistance["poison"] == True
    subrace_obj = create_subrace_object("mountain dwarf")
    c.apply_subrace_bonus(subrace_obj)
    assert c.subrace == "mountain dwarf"
    assert c.strength == 10
    assert c.proficiencies["light armor"] == True
    assert c.proficiencies["medium armor"] == True
def test_apply_dragon_subrace():
    c = Character("testing")
    assert c.strength == 8
    assert c.charisma == 8
    dragon_obj = create_race_object(dragonborn)
    c.apply_race_bonus(dragon_obj)
    assert c.speed == 30
    assert c.strength == 10
    assert c.charisma == 9
    subrace_obj = create_dragoncolor_object("black")
    c.apply_subrace_bonus(subrace_obj)
    assert c.subrace == "black"
    assert c.damage_resistance["acid"] == True
    assert c.race_info[0] == "Breath shape: line"

def test_get_spell_list():
    pass

def test_race_info_initialized():
    c = Character("testing")
    assert c.race_info == []

def test_apply_subrace_bonus_empty_list():
    c = Character("testing")
    c.race_info = []
    dragon_obj = create_race_object(dragonborn)
    c.apply_race_bonus(dragon_obj)
    subrace_obj = create_dragoncolor_object("black")
    c.apply_subrace_bonus(subrace_obj)
    assert len(c.race_info) == 3
    assert 'Breath shape: line' in c.race_info
    assert 'Breath size: (5, 30)' in c.race_info
    assert 'Breath type: acid' in c.race_info

def test_apply_subrace_bonus_multiple_calls():
    c = Character("testing")
    dragon_obj = create_race_object(dragonborn)
    c.apply_race_bonus(dragon_obj)
    subrace_obj1 = create_dragoncolor_object("black")
    subrace_obj2 = create_dragoncolor_object("white")
    c.apply_subrace_bonus(subrace_obj1)
    c.apply_subrace_bonus(subrace_obj2)
    assert len(c.race_info) == 6
    assert 'Breath shape: line' in c.race_info
    assert 'Breath size: (5, 30)' in c.race_info
    assert 'Breath type: acid' in c.race_info
    assert 'Breath shape: cone' in c.race_info
    assert 'Breath size: (15,)' in c.race_info
    assert 'Breath type: cold' in c.race_info